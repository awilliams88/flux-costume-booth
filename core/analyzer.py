from __future__ import annotations

from collections.abc import Callable
from typing import Any

try:
    import spaces
except ImportError:
    # Use a no-op GPU decorator during local development.
    class _LocalSpacesFallback:
        @staticmethod
        def GPU(
            duration: int = 60,
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
            def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
                return function

            return decorator

    spaces = _LocalSpacesFallback()

from core.inference import (
    build_costume_prompt,
    generate_costume_image,
    transcribe_audio,
)
from core.parser import stringify_content, validate_image_path
from env.config import MODEL_ID, PARAMETER_COUNT, PROMPT_LIMIT


def plan_costume(
    portrait: object | None,
    idea: Any,
    voice_idea: object | None,
    theme: str,
    intensity: Any,
    keepsake: bool,
    size: str,
    steps: Any,
    seed: Any,
) -> tuple[str | None, str, str]:
    """Orchestrates prompt building, optional speech transcription, and FLUX generation."""
    # Normalize inputs before dispatching to the GPU-backed generator.
    portrait_path, portrait_status = validate_image_path(portrait)
    typed_idea = stringify_content(idea)[:PROMPT_LIMIT]
    transcript, transcript_log = transcribe_audio(voice_idea)
    try:
        intensity_value = min(10.0, max(1.0, float(intensity)))
    except (TypeError, ValueError):
        intensity_value = 6.0
    try:
        step_count = min(40, max(8, int(steps)))
    except (TypeError, ValueError):
        step_count = 24
    try:
        seed_value = int(seed)
    except (TypeError, ValueError):
        seed_value = 42

    # Keep sizes simple and Space-friendly.
    width, height = (768, 1024) if size == "Portrait" else (1024, 768)
    prompt = build_costume_prompt(
        typed_idea,
        transcript,
        theme,
        intensity_value,
        keepsake,
    )
    output_path, generation_log = generate_costume_image(
        prompt,
        portrait_path,
        width,
        height,
        step_count,
        seed_value,
    )
    logs = "\n".join(
        [
            f"Primary model: {MODEL_ID}",
            f"Parameters: {PARAMETER_COUNT}",
            "Execution flow: local Space GPU when available; no external image API",
            "---",
            portrait_status,
            transcript_log,
            generation_log,
        ]
    )
    return output_path, prompt, logs


@spaces.GPU(duration=90)
def plan_costume_ui(
    portrait: object | None,
    idea: Any,
    voice_idea: object | None,
    theme: str,
    intensity: Any,
    keepsake: bool,
    size: str,
    steps: Any,
    seed: Any,
) -> tuple[str | None, str, str]:
    """Gradio-compatible ZeroGPU entry point for costume generation."""
    # Return image path, final prompt, and diagnostics.
    return plan_costume(
        portrait,
        idea,
        voice_idea,
        theme,
        intensity,
        keepsake,
        size,
        steps,
        seed,
    )


def reset_outputs() -> tuple[None, str, str]:
    """Clears the preview before a fresh generation run."""
    # Keep UI feedback immediate while FLUX loads.
    return None, "Composing booth prompt...", "Starting local generation..."

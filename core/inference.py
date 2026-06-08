from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from env.config import ADAPTER_REPO_ID, MODEL_ID, NEGATIVE_PROMPT, SPEECH_MODEL_ID

# Keep expensive pipelines warm after the first request.
_pipeline: Any = None
_speech_pipeline: Any = None


def transcribe_audio(audio_path: object | None) -> tuple[str, str]:
    """Transcribes optional microphone costume ideas into text."""
    global _speech_pipeline
    if not audio_path:
        return "", "No microphone input provided."
    try:
        from transformers import pipeline

        if _speech_pipeline is None:
            _speech_pipeline = pipeline(
                "automatic-speech-recognition",
                model=SPEECH_MODEL_ID,
                token=os.environ.get("HF_TOKEN"),
            )
        result = _speech_pipeline(str(audio_path))
        return str(
            result.get("text", "")
        ).strip(), f"Transcribed with {SPEECH_MODEL_ID}."
    except Exception as exc:
        return "", f"Speech transcription unavailable: {exc}"


def build_costume_prompt(
    idea: str,
    transcript: str,
    theme: str,
    intensity: float,
    keepsake: bool,
) -> str:
    """Builds the final FLUX prompt from typed and spoken costume direction."""
    # Blend user direction with the selected booth style.
    user_direction = " ".join(
        part for part in [idea.strip(), transcript.strip()] if part
    )
    if not user_direction:
        user_direction = "a charming original costume portrait"
    keepsake_phrase = (
        "keeps the person's identity, face shape, and friendly expression recognizable"
        if keepsake
        else "leans into a stylized fantasy portrait while preserving a natural face"
    )
    return (
        f"{user_direction}, {theme} costume booth portrait, {intensity:.0f}/10 transformation intensity, "
        f"{keepsake_phrase}, detailed fabric, playful handcrafted props, clean studio lighting, "
        "sharp eyes, polished but whimsical, no text"
    )


def generate_costume_image(
    prompt: str,
    source_image_path: str | None,
    width: int,
    height: int,
    steps: int,
    seed: int,
) -> tuple[str | None, str]:
    """Runs FLUX generation locally when the runtime has the required weights."""
    global _pipeline
    log_lines: list[str] = []
    try:
        import torch
        from diffusers import FluxPipeline

        # Load FLUX lazily; adapter load is best-effort for local demos.
        if _pipeline is None:
            dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
            log_lines.append(f"Loading FLUX pipeline: {MODEL_ID}")
            _pipeline = FluxPipeline.from_pretrained(
                MODEL_ID,
                torch_dtype=dtype,
                token=os.environ.get("HF_TOKEN"),
            )
            try:
                _pipeline.load_lora_weights(
                    ADAPTER_REPO_ID,
                    token=os.environ.get("HF_TOKEN"),
                )
                log_lines.append(f"Loaded costume LoRA: {ADAPTER_REPO_ID}")
            except Exception as exc:
                log_lines.append(f"Costume LoRA unavailable: {exc}")
            if torch.cuda.is_available():
                _pipeline = _pipeline.to("cuda")
        else:
            log_lines.append("Using cached FLUX pipeline.")

        # FLUX.2 klein is used for text-to-image; source image is documented in logs.
        if source_image_path:
            log_lines.append(
                "Source portrait accepted for prompt guidance; current runtime uses text-to-image generation."
            )
        generator = torch.Generator(
            device="cuda" if torch.cuda.is_available() else "cpu"
        )
        generator = generator.manual_seed(int(seed))
        result = _pipeline(
            prompt=prompt,
            negative_prompt=NEGATIVE_PROMPT,
            width=int(width),
            height=int(height),
            num_inference_steps=int(steps),
            generator=generator,
        )
        image = result.images[0]
        output_path = Path("/tmp/flux-costume-output.png")
        image.save(output_path)
        log_lines.append("FLUX generation completed.")
        return str(output_path), "\n".join(log_lines)
    except Exception as exc:
        log_lines.append(f"FLUX generation unavailable: {exc}")
        log_lines.append("Returning the uploaded portrait as preview when available.")
        return source_image_path, "\n".join(log_lines)

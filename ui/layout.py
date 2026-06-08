from __future__ import annotations

from typing import Any
import gradio as gr
from gradio.themes import Soft

from core.analyzer import plan_costume_ui, reset_outputs
from env.config import APP_DESCRIPTION, APP_TITLE, GITHUB_URL, SPACE_URL
from ui.examples import render_examples


def get_theme() -> Any:
    """Returns the custom soft theme configured for neon carnival styling."""
    # Pair FLUX creativity with a warm magenta and cyan palette.
    return Soft(primary_hue="pink", secondary_hue="cyan", neutral_hue="slate")


def create_app() -> gr.Blocks:
    """Creates and lays out the Gradio interface for Flux Costume Booth."""
    with gr.Blocks(title=APP_TITLE) as demo:
        # Header frames the app as a usable booth, not a landing page.
        gr.Markdown(f"# {APP_TITLE}\n{APP_DESCRIPTION}", elem_id="fb-header")
        gr.Markdown(
            "Upload a portrait or invent a character from scratch. The booth turns a costume idea into a polished prompt and image.",
            elem_id="fb-kicker",
        )

        with gr.Row(elem_classes=["fb-main-grid"]):
            # Left column gathers portrait and style direction.
            with gr.Column(scale=1, elem_classes=["fb-input-panel"]):
                gr.Markdown("## Costume Controls")
                portrait_input = gr.Image(
                    label="Portrait reference",
                    type="filepath",
                    sources=["upload", "webcam", "clipboard"],
                    elem_classes=["fb-image-input"],
                )
                idea_input = gr.Textbox(
                    label="Costume idea",
                    lines=5,
                    placeholder="Describe the costume, props, era, materials, or mood.",
                    elem_id="fb-idea-input",
                )
                voice_input = gr.Audio(
                    label="Speak a costume idea",
                    sources=["microphone", "upload"],
                    type="filepath",
                    elem_classes=["fb-audio-input"],
                )
                with gr.Row(elem_classes=["fb-control-row"]):
                    theme_input = gr.Dropdown(
                        [
                            "Storybook",
                            "Pixel Carnival",
                            "Ocean Parade",
                            "Sky Workshop",
                            "Miniature Movie Poster",
                        ],
                        value="Storybook",
                        label="Theme",
                    )
                    size_input = gr.Radio(
                        ["Portrait", "Landscape"],
                        value="Portrait",
                        label="Canvas",
                    )
                intensity_input = gr.Slider(
                    minimum=1,
                    maximum=10,
                    value=6,
                    step=1,
                    label="Transformation intensity",
                )
                keepsake_input = gr.Checkbox(
                    value=True,
                    label="Keep face recognizable",
                )
                with gr.Row(elem_classes=["fb-control-row"]):
                    steps_input = gr.Slider(
                        minimum=8,
                        maximum=40,
                        value=24,
                        step=1,
                        label="Steps",
                    )
                    seed_input = gr.Number(value=42, precision=0, label="Seed")
                run_button = gr.Button(
                    "Open Booth",
                    variant="primary",
                    elem_classes=["fb-run-btn"],
                )

            # Right column displays the generated result and final prompt.
            with gr.Column(scale=1, elem_classes=["fb-output-panel"]):
                gr.Markdown("## Costume Preview")
                output_image = gr.Image(
                    label="Generated costume",
                    type="filepath",
                    interactive=False,
                    elem_classes=["fb-output-image"],
                )
                prompt_output = gr.Textbox(
                    label="Final FLUX prompt",
                    lines=7,
                    interactive=False,
                    elem_classes=["fb-prompt-output"],
                )

        render_examples(idea_input, theme_input)

        gr.Markdown(
            f"[GitHub repo]({GITHUB_URL}) | [Hugging Face Space]({SPACE_URL})",
            elem_id="fb-links",
        )

        with gr.Accordion("Diagnostics & System Execution Logs", open=False):
            model_output = gr.Textbox(
                label="System execution logs",
                lines=7,
                interactive=False,
                elem_classes=["fb-log-box"],
            )

        # Reset preview before dispatching to the GPU-backed generator.
        reset_event = run_button.click(
            fn=reset_outputs,
            inputs=[],
            outputs=[output_image, prompt_output, model_output],
            queue=False,
        )
        reset_event.then(
            fn=plan_costume_ui,
            inputs=[
                portrait_input,
                idea_input,
                voice_input,
                theme_input,
                intensity_input,
                keepsake_input,
                size_input,
                steps_input,
                seed_input,
            ],
            outputs=[output_image, prompt_output, model_output],
        )

    return demo

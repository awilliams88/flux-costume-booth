from __future__ import annotations

from html import escape
import gradio as gr

# Costume presets demonstrate style range without hard-coding generation.
EXAMPLE_CARDS = [
    {
        "title": "Moon Garden Knight",
        "theme": "Storybook",
        "idea": "silver leaf armor, soft moss cape, tiny glowing moon flowers",
    },
    {
        "title": "Retro Arcade Mage",
        "theme": "Pixel Carnival",
        "idea": "neon robe, joystick staff, 1980s arcade glow, playful confident pose",
    },
    {
        "title": "Deep Sea Baker",
        "theme": "Ocean Parade",
        "idea": "coral chef hat, kelp apron, pearl buttons, gentle underwater light",
    },
    {
        "title": "Cloud Courier",
        "theme": "Sky Workshop",
        "idea": "aviator scarf, cloud satchel, brass goggles, breezy postcard mood",
    },
]


def _card_html(title: str, theme: str, idea: str) -> str:
    """Builds a compact costume preset preview."""
    return (
        '<div class="fb-example-copy">'
        '<div class="fb-example-head">'
        f"<span>{escape(title)}</span>"
        f"<strong>{escape(theme)}</strong>"
        "</div>"
        f"<p>{escape(idea)}</p>"
        "</div>"
    )


def _select_example(idea: str, theme: str) -> tuple[str, str]:
    """Populates the prompt and theme controls from an example."""
    return idea, theme


def render_examples(idea_input: gr.Textbox, theme_input: gr.Dropdown) -> gr.Column:
    """Renders costume presets and wires their buttons."""
    with gr.Column(elem_classes=["fb-examples-section"]) as section:
        gr.Markdown("## Booth Presets")
        with gr.Row(elem_classes=["fb-example-grid"]):
            for example in EXAMPLE_CARDS:
                with gr.Column(elem_classes=["fb-example-card"]):
                    gr.HTML(
                        _card_html(
                            str(example["title"]),
                            str(example["theme"]),
                            str(example["idea"]),
                        )
                    )
                    use_example = gr.Button(
                        "Use preset",
                        size="sm",
                        elem_classes=["fb-example-btn"],
                    )
                    use_example.click(
                        fn=lambda idea=str(example["idea"]), theme=str(example["theme"]): (
                            _select_example(idea, theme)
                        ),
                        inputs=[],
                        outputs=[idea_input, theme_input],
                        queue=False,
                    )
    return section

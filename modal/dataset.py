from __future__ import annotations

# Trigger token used by the style LoRA dataset and prompt builder.
STYLE_TOKEN = "avenium_costume_booth"


def build_caption(costume: str, theme: str, details: str) -> str:
    """Builds a FLUX caption matching the production prompt style."""
    return (
        f"{STYLE_TOKEN}, {costume}, {theme} costume booth portrait, {details}, "
        "detailed fabric, playful handcrafted props, clean studio lighting, sharp eyes, no text"
    )


def get_training_captions() -> list[dict[str, str]]:
    """Returns synthetic caption seeds for a Modal FLUX LoRA image dataset."""
    return [
        {
            "file_name": "moon_garden_knight.png",
            "text": build_caption(
                "silver leaf armor and moss cape",
                "storybook",
                "tiny glowing moon flowers and gentle heroic expression",
            ),
        },
        {
            "file_name": "retro_arcade_mage.png",
            "text": build_caption(
                "neon robe and joystick staff",
                "pixel carnival",
                "arcade glow, saturated playful color, confident pose",
            ),
        },
        {
            "file_name": "deep_sea_baker.png",
            "text": build_caption(
                "coral chef hat and kelp apron",
                "ocean parade",
                "pearl buttons, underwater light, friendly keepsake portrait",
            ),
        },
        {
            "file_name": "cloud_courier.png",
            "text": build_caption(
                "aviator scarf and cloud satchel",
                "sky workshop",
                "brass goggles, breezy postcard mood, polished whimsical texture",
            ),
        },
        {
            "file_name": "library_dragon_scholar.png",
            "text": build_caption(
                "emerald scholar robe with tiny dragon shoulder cape",
                "storybook",
                "old library warmth, brass bookmark pins, friendly clever expression",
            ),
        },
        {
            "file_name": "rainy_neon_detective.png",
            "text": build_caption(
                "transparent raincoat, neon magnifying glass, reflective boots",
                "miniature movie poster",
                "rain-slick pavement colors, cinematic but wholesome mystery mood",
            ),
        },
        {
            "file_name": "desert_teacup_ranger.png",
            "text": build_caption(
                "sun-faded ranger poncho and porcelain teacup badge",
                "storybook",
                "warm sand light, embroidered cactus trim, keepsake portrait realism",
            ),
        },
        {
            "file_name": "clockwork_florist.png",
            "text": build_caption(
                "copper floral apron, gear-shaped boutonniere, wind-up watering can",
                "sky workshop",
                "soft brass highlights, handmade costume details, gentle smile",
            ),
        },
        {
            "file_name": "candy_planet_captain.png",
            "text": build_caption(
                "licorice captain coat and gumdrop epaulets",
                "pixel carnival",
                "bright playful candy colors, crisp studio portrait, polished props",
            ),
        },
        {
            "file_name": "aurora_train_conductor.png",
            "text": build_caption(
                "midnight conductor jacket and aurora ticket punch",
                "miniature movie poster",
                "glowing northern lights trim, theatrical train-station atmosphere",
            ),
        },
        {
            "file_name": "mushroom_orchestra_maestro.png",
            "text": build_caption(
                "velvet maestro coat and mushroom-cap baton",
                "storybook",
                "tiny woodland orchestra hints, textured fabric, expressive eyes",
            ),
        },
        {
            "file_name": "solar_punk_gardener.png",
            "text": build_caption(
                "leafy utility vest, sunflower visor, seed-packet sash",
                "sky workshop",
                "clean optimistic light, natural materials, recognizable friendly face",
            ),
        },
    ]

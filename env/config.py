from __future__ import annotations

# App copy shown in the Gradio header.
APP_TITLE = "Flux Costume Booth"
APP_DESCRIPTION = "Playful portrait transformations with compact FLUX styling."

# Input constraints keep generation prompts focused.
PROMPT_LIMIT = 1800
NEGATIVE_PROMPT = "blurry, distorted face, extra fingers, text watermark, low quality"
SUPPORTED_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}

# Public links shown in the Space footer.
GITHUB_URL = "https://github.com/awilliams88/flux-costume-booth"
SPACE_URL = "https://huggingface.co/spaces/build-small-hackathon/flux-costume-booth"

# Model metadata keeps docs, logs, and UI aligned.
MODEL_ID = "black-forest-labs/FLUX.2-klein-4B"
ADAPTER_REPO_ID = "build-small-hackathon/flux-costume-booth-lora"
SPEECH_MODEL_ID = "openai/whisper-small"
SPONSOR_NAME = "Black Forest Labs / Modal"
PARAMETER_COUNT = "4B"

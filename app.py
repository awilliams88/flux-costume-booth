from __future__ import annotations

import os
from env.runtime import patch_asyncio_cleanup_warning
from ui.layout import create_app, get_theme
from ui.styles import CUSTOM_CSS

# Disable SSR noise for custom Gradio styling on Spaces.
os.environ.setdefault("GRADIO_SSR_MODE", "false")

# Hide a harmless local Gradio cleanup warning.
patch_asyncio_cleanup_warning()

# Build the Space app once for Gradio discovery.
demo = create_app()

if __name__ == "__main__":
    # Keep direct launch available for run.sh and Spaces.
    demo.launch(theme=get_theme(), css=CUSTOM_CSS)

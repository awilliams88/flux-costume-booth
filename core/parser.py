from __future__ import annotations

from pathlib import Path
from typing import Any

from env.config import SUPPORTED_IMAGE_SUFFIXES


def resolve_path(file_input: object | None) -> Path | None:
    """Normalizes Gradio file payload variants into a local path."""
    # Empty uploads are valid for text-to-image mode.
    if not file_input:
        return None
    if isinstance(file_input, (list, tuple)):
        for item in file_input:
            path = resolve_path(item)
            if path:
                return path
        return None
    if isinstance(file_input, dict):
        for key in ("path", "name", "orig_name"):
            value = file_input.get(key)
            if value:
                return Path(str(value))
        return None
    return Path(str(file_input))


def validate_image_path(file_input: object | None) -> tuple[str | None, str]:
    """Returns a usable portrait path and human-readable validation status."""
    # Text-to-image generation does not require a source image.
    path = resolve_path(file_input)
    if not path:
        return None, "No source portrait uploaded; using text-to-image mode."
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_IMAGE_SUFFIXES:
        return None, f"Unsupported portrait format: {suffix}."
    if not path.exists():
        return None, "Uploaded portrait was not found in the local runtime."
    return str(path), f"Portrait accepted: {path.name}"


def stringify_content(content: Any) -> str:
    """Converts Gradio content variants into prompt-safe text."""
    # Plain textbox values arrive as strings.
    if content is None:
        return ""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, (list, tuple)):
        parts = [stringify_content(item) for item in content]
        return " ".join(part for part in parts if part).strip()
    if isinstance(content, dict):
        for key in ("text", "value", "path", "url", "name", "alt_text"):
            value = content.get(key)
            if value:
                return stringify_content(value)
        return ""
    return str(content).strip()

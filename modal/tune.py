from __future__ import annotations

import json
import os
from typing import Any

import modal

modal_any: Any = modal

# Modal app groups the remote FLUX LoRA preparation job.
app = modal_any.App("flux-costume-booth-tuner")

# Container includes diffusers training dependencies and local caption code.
image = (
    modal_any.Image.debian_slim()
    .pip_install(
        "torch",
        "transformers>=4.45.0",
        "diffusers",
        "accelerate",
        "peft",
        "datasets",
        "safetensors",
        "huggingface_hub",
        "pillow",
    )
    .add_local_file(
        os.path.join(os.path.dirname(__file__), "dataset.py"),
        "/root/dataset.py",
    )
)

# Volume keeps generated dataset metadata and checkpoints available.
volume = modal_any.Volume.from_name("flux-costume-checkpoints", create_if_missing=True)

MODEL_ID = "black-forest-labs/FLUX.2-klein-4B"
ADAPTER_REPO_ID = "build-small-hackathon/flux-costume-booth-lora"


@app.function(
    image=image,
    gpu="A10G",
    timeout=10800,
    volumes={"/checkpoints": volume},
    secrets=[modal_any.Secret.from_name("huggingface-secret")],
)
def prepare_lora_run(model_card_content: str, hf_token: str | None = None):
    """Prepares the app-format FLUX LoRA dataset and publishes metadata for manual training."""
    # Remote-only imports are installed inside the Modal container.
    import io
    import os as remote_os

    from huggingface_hub import HfApi, login, upload_file

    from dataset import get_training_captions

    # This project uses Modal for the heavy FLUX LoRA run; this function validates and stages data.
    captions = get_training_captions()
    os.makedirs("/checkpoints/flux-costume-dataset", exist_ok=True)
    metadata_path = "/checkpoints/flux-costume-dataset/metadata.jsonl"
    with open(metadata_path, "w", encoding="utf-8") as f:
        for item in captions:
            f.write(json.dumps(item) + "\n")
    volume.commit()
    print(f"Prepared {len(captions)} app-format FLUX caption records.")
    print(
        "Training target: current production prompt format with avenium_costume_booth trigger token."
    )

    # Publish the model card so the adapter repository is ready before manual image training.
    hf_token = hf_token or remote_os.environ.get("HF_TOKEN")
    if hf_token:
        login(token=hf_token)
        api = HfApi(token=hf_token)
        api.create_repo(ADAPTER_REPO_ID, repo_type="model", exist_ok=True)
        upload_file(
            path_or_fileobj=io.BytesIO(model_card_content.encode("utf-8")),
            path_in_repo="README.md",
            repo_id=ADAPTER_REPO_ID,
            repo_type="model",
            commit_message="Update Flux Costume Booth LoRA model card",
        )
    else:
        print("HF_TOKEN not set. Skipping Hub publish.")


@app.local_entrypoint()
def main():
    # Read CARD.md dynamically so latest metadata is included in the run.
    meta_path = os.path.join(os.path.dirname(__file__), "CARD.md")
    with open(meta_path, encoding="utf-8") as f:
        model_card = f.read()
    prepare_lora_run.remote(model_card_content=model_card)

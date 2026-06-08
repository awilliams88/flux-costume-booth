---
base_model: black-forest-labs/FLUX.2-klein-4B
library_name: diffusers
pipeline_tag: text-to-image
language:
- en
tags:
- flux
- lora
- costume
- portrait
- modal
- build-small-hackathon
---

# Flux Costume Booth LoRA

Flux Costume Booth LoRA is the planned style adapter for the Flux Costume Booth
Space. It targets a playful handcrafted portrait-booth style using the trigger
token `avenium_costume_booth`.

## Intended Use

- Whimsical costume portrait generation
- Keepsake-style photo booth transformations
- Themed creative demos for Build Small Hackathon

## Training Plan

- Base model: `black-forest-labs/FLUX.2-klein-4B`
- Method: FLUX LoRA
- Hardware: Modal NVIDIA A10G or better
- Dataset: curated costume portrait captions plus matching generated/curated images
- Output: Diffusers-compatible LoRA adapter
- Production prompt target: current app prompt format with theme, intensity, and identity-preservation language

## Limitations

The adapter is for playful portrait styling. It should not be used for deceptive
identity impersonation, explicit imagery, or harmful stereotypes.

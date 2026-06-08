---
title: Flux Costume Booth
emoji: 🎭
colorFrom: pink
colorTo: blue
sdk: gradio
sdk_version: 6.17.3
app_file: app.py
python_version: "3.12"
short_description: Playful portrait transformations with compact FLUX styling
pinned: false
tags:
- build-small-hackathon
- thousand-token-wood
- black-forest-labs
- modal
- off-brand
- off-the-grid
- well-tuned
- best-demo
- text-to-image
---

# Flux Costume Booth

Flux Costume Booth is a playful portrait transformation Space. Users can upload
a portrait, type or speak a costume idea, choose a booth theme, and generate a
polished FLUX prompt and costume image.

## Model Plan

- Primary model: `black-forest-labs/FLUX.2-klein-4B`
- Speech input: `openai/whisper-small` local transcription
- Fine-tuned adapter: `build-small-hackathon/flux-costume-booth-lora`
- Training: Modal-hosted FLUX LoRA workflow
- Parameter cap: FLUX.2 klein is a 4B model, under the 32B hackathon limit

The app generates locally inside the Space runtime. If FLUX weights or adapter
loading fail, it returns the uploaded portrait preview and logs the issue clearly.

## Hackathon Alignment

| Requirement | Flux Costume Booth implementation |
|---|---|
| Gradio Space in `build-small-hackathon` | `build-small-hackathon/flux-costume-booth` |
| Track | Thousand Token Wood |
| Sponsor focus | Black Forest Labs FLUX.2 klein and Modal LoRA workflow |
| Merit targets | Well-Tuned, Off-Brand, Best Demo, Off the Grid |
| Multimodal input | Portrait upload/webcam, typed costume idea, microphone transcript |
| Modal usage | Modal stages the FLUX LoRA caption dataset and adapter repo metadata |
| Demo/social links | Add final demo video and social post links after recording |

## Links

- GitHub Repo: https://github.com/awilliams88/flux-costume-booth
- Hugging Face Space: https://huggingface.co/spaces/build-small-hackathon/flux-costume-booth
- Fine-tuned Model: https://huggingface.co/build-small-hackathon/flux-costume-booth-lora
- Demo Video: pending final recording
- Social Post: pending final post

## Local Development

```bash
./run.sh setup
./run.sh app
./run.sh verify
```

## Codebase

| Path | Purpose |
|---|---|
| `app.py` | Hugging Face Spaces entry point |
| `env/` | Runtime patches, model IDs, limits, links |
| `core/` | Prompt construction, optional speech transcription, FLUX inference |
| `ui/` | Gradio booth layout, presets, neon costume CSS |
| `modal/` | Modal LoRA staging job, caption dataset, model card |

## Safety

This project is for playful, consensual portrait styling. It should not be used
for deceptive impersonation, explicit content, or harmful stereotypes.

## Training Data

The Modal dataset defines a consistent `avenium_costume_booth` trigger style with
storybook, pixel carnival, ocean parade, sky workshop, and miniature movie poster
captions. The data targets the current production prompt format with theme,
intensity, and identity-preservation language.

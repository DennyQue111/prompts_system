# Sequence (Scene-Level Composition)

## What This Is
Records the prompt structure for generating a **sequence** — a scene-level prompt that describes how multiple shots connect and flow together. Used for video generation models that understand narrative progression across shots.

## Available Files

| File | What It Is |
|------|-------------|
| `seedance.md` | Sequence architecture for Seedance / 即梦 (shot-based, structured fields, negative constraints) |
| `minimax.md` | Sequence architecture for MiniMax H3 (time-segment-based, inline image refs, positive-only, sound design) |
| `examples.md` | Worked examples of sequence prompts |

## Usage
- If the user wants Seedance / 即梦 → use `seedance.md`
- If the user wants MiniMax H3 → use `minimax.md`
- Individual shots within a sequence should reference the shot architecture in `../shot/`

## Model Selection Guide

| Model | Sequence File | Shot File | Key Differences |
|-------|--------------|-----------|-----------------|
| Seedance / 即梦 | `seedance.md` | `../shot/seedance.md` | Shot-based, negative constraints, @image block, no sound |
| MiniMax H3 | `minimax.md` | `../shot/minimax.md` | Time-segment-based, positive-only, inline @图片N, sound design, strict punctuation |

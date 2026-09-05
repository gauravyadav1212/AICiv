# AI Civ

A terminal-based simulation where LLM-driven NPCs live in a shared medieval world. Each character has a persistent "soul" (personality, goals, fears, beliefs, role), reacts to events, forms memories, and decides how to act — all through a local LLM.

## How it works

- **Souls** (`npc/soul.py`) define who a character is: personality traits, goals, fears, beliefs, gender, and social role (`enums/roles.py`, `enums/gender.py`).
- **Characters** (`npc/character.py`) wrap a soul with a location, a memory list, and an `LLMEngine`. They can `observe` events (forming a `Memory` with an emotion and importance score) or `think` about a situation and return a JSON action.
- **Memories** (`npc/memory.py`) are saved to and loaded from `data/<name>_memories.json`, so a character's recollections persist between runs.
- **Locations** (`world/location.py`) have a description, type, social class, danger level, lore, rumors, an owner, and can connect to other locations.
- **World** (`world/world.py`) owns all characters and locations, broadcasts events to characters at a location (or globally), and drives the simulation loop by asking each character what they'd do next.
- **LLM engine** (`llm/llm_engine.py`) talks to a local model via [Ollama](https://ollama.ai) (`langchain-ollama`), forcing JSON-formatted responses.

## Requirements

- [uv](https://docs.astral.sh/uv/) (manages the Python version and virtual environment — no separate Python install needed)
- [Ollama](https://ollama.ai) installed and running locally, with a model pulled (the default is `mistral:latest`):
  ```
  ollama pull mistral
  ```

## Setup

```
uv sync
```

This creates `.venv` and installs the pinned dependencies from `uv.lock`.

## Running

```
uv run main.py
```

`main.py` sets up a small cast of characters (an earl, a knight, a tavern keeper, a marshal) in a starting location, prints the world state, then asks you for an initial event to broadcast. Each character reacts, and pressing Enter advances the simulation — every character decides on and prints their next thought/action/target — until you type `exit`.

## Status

This is an early-stage experiment. Current building blocks: souls, characters, memories, locations, and a world loop. Not yet implemented: conversations between characters beyond `conversation_manager.py`'s round-robin exchange, richer multi-location movement, and persistent world/location state across runs.

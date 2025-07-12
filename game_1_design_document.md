# Game 1 Design Document: Post-Civilization Procedural RPG

---

## Table of Contents
1. Overview & Vision
2. Setting & Themes
3. Gameplay Mechanics
4. World Generation
5. Item, Crafting & Materials System
6. NPCs & AI Systems
7. Story Structure & Story Anchors
8. Procedural Storytelling with LLMs
9. Art Direction & Assets
10. Technical Stack & Tools
11. Roadmap & Modular Development
12. Appendices (Reference Lists, Flowcharts)

---

## 1. Overview & Vision

- **Working Title:** After the Fall
- **Genre:** Procedural Top-down RPG (inspired by RimWorld, Dwarf Fortress, Unreal World, Ultima)
- **Core Loop:** Survival, exploration, crafting, and social storytelling in a world where knowledge of the past is lost.
- **Replayability:** High. Procedural world and dynamic events. No two playthroughs are the same.

## 2. Setting & Themes

- 7500+ years after the collapse of advanced society (WWIII + climate disaster).
- Civilization is primitive, medieval-like. Megalithic ruins remain; 21st-century cities are dust.
- Castles, kings, emperors, and slaves; society is brutal and raw, but with human resilience.
- The player is just another character—a villager, smith, wanderer—no "chosen one."

## 3. Gameplay Mechanics

### Core Systems
- **Top-down 2D tile-based world** with full procedural generation.
- **All items, tiles, and resources are destructible/buildable.**
- **Survival:** Hunger, thirst, temperature, wounds, disease, and social status.
- **Crafting:** Layered, modular system—everything from basic tools to complex structures.
- **Inventory:** Weight, volume, and item-specific properties. Items can be nested (chests, bags).
- **Combat:** Simple (melee, ranged, thrown) but deeply influenced by item/material stats.
- **Impressiveness stat:** Affects NPC perception, dialogue, and status.
- **Replayable, semi-randomized events and quests.**

### Modular Systems
- Tile-based world = groupable tiles for houses, walls, terrain, villages.
- Item system: Fully extensible via JSON/YAML definitions.
- LLM-driven storytelling for dialogue and quests.
- Modding support for events, items, and tilemaps.

## 4. World Generation

- **Procedurally generated tile map** (Perlin noise for biomes: forest, hills, rivers, plains).
- **Settlements:** Villages, castles, ruins, dungeons, trade posts.
- **Megalithic ruins:** Uniquely placed, indestructible or hard-to-destroy tiles.
- **Destructibility:** Everything but ancient megaliths can be destroyed, moved, or rebuilt.
- **Grouping system:** Tiles can represent single objects or be grouped into larger objects (houses, mountains, ships, etc).

## 5. Item, Crafting & Materials System

### Base Materials (Mineable/Scavengeable)
- Iron, Copper, Tin, Gold, Silver, Lead, Stone, Clay, Wood, Leather, Textiles, Plant Fibers, Bone, Obsidian, Coal, Sand, Salt, Marble, Granite, (others).

### Intermediate & Advanced Materials
- Bronze (Copper+Tin), Steel (Iron+Coal), Glass (Sand+Fire), Glue (Bone+Water), etc.

### Item Types
- Tools (axe, pick, shovel, knife, hammer, etc)
- Weapons (sword, dagger, mace, spear, bow, sling)
- Armor (helmet, cuirass, boots, shield)
- Wearables (clothes, rings, necklaces)
- Consumables (food, water, medicine, bandages)
- Containers (bag, chest, crate, jar)
- Structures (door, wall, roof, floor, window)

### Item Stats
- Material type(s), weight, volume, durability, age, quality, rarity, impressiveness.
- Hardcoded stats + dynamically calculated (based on material, type, size).
- Equip slots: hand, head, torso, feet, etc.

### Crafting
- Multi-layered recipes (JSON/YAML):
  - Base resources → Intermediate components → Final items.
- Crafting stations: anvil, firepit, loom, kiln.
- Some recipes require blueprints or high skill.

## 6. NPCs & AI Systems

### Types
- Villagers, lords, guards, smiths, farmers, traders, bandits, wild animals, slaves, travelers.

### Behavior
- Needs (food, water, rest, safety, social, status).
- Personality traits: shy, aggressive, curious, eccentric, etc.
- Emotional state: affects behavior and dialogue.
- Grouping: Families, villages, factions. Groups can have goals (defense, work, party, etc).

### Movement & Animation
- Pathfinding (A* or similar), avoidance, idle, work, social, sleep.
- Animations mapped to states: idle, walk, angry, excited, sitting, etc.

### RL/ML Extensions (for advanced builds)
- NPCs can be trained (optionally) using RL for behaviors or emergent tasks (walking, reacting, socializing).
- Behavior and dialogue seeded from LLM output (if available).

## 7. Story Structure & Story Anchors

- **Player = Any NPC**: No fixed hero; all characters equal, player controls one.
- **Anchors:**
  - *Hard Goals*: Must occur to progress/complete the saga (e.g., destruction of starting house, discovery of City of Light).
  - *Soft Goals*: Optional, rewarding, emergent (find a relic, solve a dispute, build a monument).
- **Story Bot** (LLM or procedural system) monitors the world, nudges it toward hard goals (by events, disasters, invasions, NPCs).
- Each anchor has multiple triggers, possible actors, and flexible outcomes.
- Player may witness, cause, or miss anchor events.

## 8. Procedural Storytelling with LLMs

- If LLM is present, it:
  - Generates dialogue, descriptions, and dynamic quests within world constraints.
  - Suggests and injects NPCs, rumors, or events to achieve hard/soft goals.
  - Adjusts narrative to player actions (sandbox style).
- If no LLM, story/quests are generated procedurally from world state and anchor logic.
- LLM is modular/optional—game runs on pure procedural/seed-based logic if needed.

## 9. Art Direction & Assets

- Top-down pixel art or minimalist tileset.
- Characters and tiles are modular and customizable (hair, clothes, items, colors).
- Color palette: Muted earth tones, bright highlights for rare/legendary items.
- Sprite sheets: Items and characters split into layers (base + overlays for materials/colors).
- Placeholder art packs: Kenney’s, OpenGameArt, custom generated (AI/Stable Diffusion).

## 10. Technical Stack & Tools

- **Engine:** Godot 4.x
- **Language:** GDScript (Python-like), optionally C# for modules
- **Core Plugins:**
  - Inventory System 2.5.5
  - Godot-BehaviorTree or custom FSM for AI
  - TileMap, Grid, Pathfinder
  - Modding/JSON loader for assets, items, recipes
- **Optional LLM Integration:**
  - Godot-LLM plugin (for offline/packaged open source models)
  - User API key or local LLM (Olama, LM Studio)
- **Testing:** Godot built-in test framework, manual playtesting
- **Art Pipeline:** Stable Diffusion/ComfyUI for asset generation
- **Version Control:** Git

## 11. Roadmap & Modular Development

- **Step 1:** Engine, worldgen, and tilemap setup
- **Step 2:** Inventory, items, and basic crafting
- **Step 3:** NPCs, AI, and basic needs simulation
- **Step 4:** Story anchors, event system, and procedural questing
- **Step 5:** Art/style pass and UI/UX
- **Step 6:** Advanced AI, LLM hooks, modding

## 12. Appendices

### Reference Lists
- **Base Materials:** Iron, Copper, Tin, Stone, Wood, Leather, etc.
- **Intermediate Materials:** Bronze, Steel, Glass, Glue, etc.
- **Item Types:** Swords, axes, spears, armor, shields, clothes, rings, bags, food, etc.

### Flowcharts & Diagrams
- Procedural worldgen flow
- Item/material crafting tree
- Story anchor/event trigger system
- NPC interaction/behavior tree

---

# END OF DOCUMENT


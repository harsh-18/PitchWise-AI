# PitchWise — Project Summary

**Hackathon:** IBM TechXchange / Call for Code 2025  
**Category:** AI for Fan Experience / Explainable AI  
**Built with:** Python, Streamlit, IBM Bob

---

## What It Does

PitchWise is a live World Cup match explainer. It takes a fixture, a set of contextual inputs, and a match event — and produces a layered, human-readable explanation of what is happening tactically, why momentum may shift, and how to interpret key decisions honestly.

It is not a scoreline predictor. It is an explanation engine.

---

## The Problem It Solves

World Cup matches are watched by billions of people across wildly different levels of football knowledge. Most AI tools in this space output predictions or statistics without explaining what they mean or why they matter. Fans — especially new or casual viewers — are left with numbers but no understanding.

PitchWise closes that gap.

---

## How It Works

| Layer | What it does |
|---|---|
| **Contextual scoring model** | Scores each team across five weighted dimensions: attack (28%), defense (22%), midfield (22%), recent form (18%), pressure handling (10%) |
| **Context adjustments** | Venue atmosphere and tournament pressure level modify the base score |
| **Narrative generation** | The score gap drives a tiered match story: closely matched, moderate edge, or clear structural advantage |
| **Fan-level adaptation** | The same tactical analysis is re-expressed for beginner, casual fan, or analyst audiences |
| **Event interpretation** | Each match event (red card, VAR, substitution, etc.) is explained through both a momentum lens and a trust/transparency lens |

Every factor is named, weighted, and visible. There is no black box.

---

## Why It Matters

- **Fan understanding** — explains *why* things happen, not just *that* they happened
- **Transparent AI** — all inputs and weights are shown; the user can agree or challenge every reading
- **Accessibility** — adapts analysis depth to how the fan actually watches the game
- **Scalability** — the architecture extends naturally to live event feeds, multilingual output, and IBM Granite-powered narrative generation

---

## IBM Technology

PitchWise was designed, built, and refined using **IBM Bob**, IBM's AI-supported development assistant. IBM Bob was used throughout the prototyping cycle for code generation, UI refinement, explainability framing, and documentation.

---

## Running the Demo

```bash
pip install -r requirements.txt
streamlit run app.py
```

No API keys. No external services. Runs fully offline.

# PitchWise

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b.svg)](https://streamlit.io)
[![GitHub](https://img.shields.io/badge/GitHub-pitchwise--explain--the--match-181717.svg)](https://github.com/harsh-18/pitchwise-explain-the-match)

PitchWise is an explainable World Cup match companion that helps fans understand the story behind a match, not just the score or prediction.

## Live Demo

> **Live:** [https://pitchwise-explain-the-match.streamlit.app](https://pitchwise-explain-the-match.streamlit.app)
>
> To run locally: `pip install -r requirements.txt && streamlit run app.py`

## Problem

World Cup matches are watched by billions of people, but fans understand them differently depending on language, tactical knowledge, culture, emotional investment, and trust in decisions. Many tools show scores or predictions, but they do not explain why a match feels like it is changing.

## Solution

PitchWise gives fans a simple, explainable match interpretation experience. Users choose two teams, match context, fan knowledge level, pressure level, and a key match event. The app then explains:

- which team has contextual advantages
- why the model leans one way
- how momentum may shift after events such as red cards, penalties, substitutions, VAR reviews, or tactical shape changes
- how the explanation should change for beginners, casual fans, or analysts

## IBM Technology Used

This prototype uses **IBM Bob** as the IBM AI-supported development tool. IBM Bob was used to help design, build, and refine the Streamlit prototype quickly for the challenge.

## AI / Technical Approach

The prototype uses an explainable scoring model based on team attributes:

- attack
- defense
- midfield control
- recent form
- pressure handling
- venue context
- match pressure

Instead of acting as a pure outcome predictor, PitchWise converts those factors into transparent explanations. The app generates different match narratives depending on the fan's knowledge level and the selected match event.

This keeps AI central to the user experience while focusing on understanding, explainability, trust, and accessibility rather than replacing coaches, referees, or players.

## Why It Matters

The World Cup is not only about results. It is about interpretation, emotion, debate, and shared meaning. PitchWise helps fans understand tactical shifts, pressure moments, and controversial events in clearer language, making soccer analysis more accessible at global scale.

## What This Project Avoids

PitchWise is not:

- a pure score prediction engine
- a referee replacement
- a coach replacement
- a fantasy or trivia app
- an opaque black-box model

It is a human-centered explanation tool.

## Project Files

| File | Purpose |
|---|---|
| [`app.py`](app.py) | Full Streamlit application — all logic, scoring model, and UI |
| [`requirements.txt`](requirements.txt) | Python dependencies |
| [`PROJECT_SUMMARY.md`](PROJECT_SUMMARY.md) | One-page brief for hackathon judges |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution guidelines |
| [`LICENSE`](LICENSE) | MIT License |

## How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
streamlit run app.py
```

## Demo Script

1. Select two World Cup teams.
2. Choose the fan knowledge level.
3. Adjust venue and pressure context.
4. Select a match event such as VAR review, red card, or substitution.
5. Show the probability-style outlook, the factor explanation, the fan-friendly explanation, and the trust/transparency lens.

## Future Improvements

- Add IBM Granite for live natural-language explanation generation.
- Add LangFlow or LangChain orchestration for event-specific explanation chains.
- Add multilingual explanations for global World Cup audiences.
- Add real match event feeds and post-match report generation.

## License

[MIT](LICENSE) © 2025 harsh-18

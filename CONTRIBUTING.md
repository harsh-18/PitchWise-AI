# Contributing to PitchWise

Thank you for your interest in contributing. This is a hackathon prototype, so the bar for contributions is practical and focused.

## Getting started

1. Fork the repository and clone your fork.
2. Create a branch: `git checkout -b your-feature-name`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app locally: `streamlit run app.py`

## What to contribute

- **New team profiles** — add entries to `TEAM_PROFILES` in `app.py` following the existing schema.
- **New match events** — add entries to `EVENT_EXPLANATIONS` with both a `momentum` and a `trust` key.
- **Improved narrative logic** — refine `match_story()`, `fan_explanation()`, or `explain_feature()`.
- **Bug fixes** — open an issue first if the fix is non-trivial.

## What to avoid

- Do not add external API dependencies, paid services, or secrets to the codebase.
- Do not change the explainability-first design intent — PitchWise is an explanation engine, not a prediction engine.
- Do not submit large refactors without a prior discussion in an issue.

## Pull requests

- Keep PRs focused — one logical change per PR.
- Describe what you changed and why in the PR description.
- The app must run cleanly with `streamlit run app.py` before submitting.

## Code style

Follow the existing style in `app.py`: section comments, docstring-free short functions, and plain readable variable names.

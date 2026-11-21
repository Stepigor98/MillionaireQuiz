# DESIGN.md

## Project

Millionaire Quiz

## Framework and scope

This document describes the **optional Streamlit 50/50 demonstration** in `MillionaireQuiz_Folder/ui/lifeline_demo.py`, not the main desktop application. The main Millionaire Quiz game uses **Tkinter**.

## Colors

| Element | Color |
|---|---|
| Background | `#0F172A` |
| Card | `#111827` |
| Primary button | `#F5C542` |
| Secondary color | `#1E3A8A` |
| Text | `#F8FAFC` |
| Muted text | `#CBD5E1` |
| Success | `#22C55E` |
| Warning | `#F97316` |

## Typography

- Use simple readable text.
- Main title should be big and bold.
- Question text should be clear.
- Do not use decorative fonts.

## Spacing

- Use enough space between question, answers and buttons.
- Answer options should be shown as separate blocks.
- The page should not look overloaded.

## Component Rules

- Buttons should have clear names.
- Main button is used for the 50/50 lifeline.
- Answer options should be displayed as cards.
- Result message should be visible after clicking the button.
- The UI should not duplicate backend logic.

## Backend Connection

The UI must use the existing module from Task 4:

```python
from lifelines.strategies import FiftyFiftyStrategy, LifelineContext

```

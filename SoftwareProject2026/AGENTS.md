# AGENTS.md

## Project Overview

- This repository contains a Software Engineering course project called **Millionaire Quiz**.
- The project is a desktop quiz game inspired by “Who Wants to Be a Millionaire”.
- The application is developed in **Python**.
- The user interface is built with **Tkinter**.
- **SQLite** is used for storing questions, game data, and future game history.
- The main goal is to improve and finalize the existing quiz game by adding settings, lifelines, game history, leaderboard, better UI, and CSV import/export.

## Important Context for AI Agents

- Always read the `/docs` folder before making changes.
- Use `/docs/pm_approach.md` to understand how the project is managed.
- Use `/docs/plans/roadmap.md` to understand the MVP plan and future development stages.
- README.md is written for humans.
- AGENTS.md is written for AI assistants.
- Do not invent new requirements if they are not written in README.md or `/docs`.

## Main Rules for AI Agents

- Keep the project simple and understandable.
- Follow the existing project structure.
- Do not create unnecessary files or folders.
- Do not rewrite the whole project without human approval.
- Do not remove existing features unless it is clearly required.
- Prefer small and safe changes instead of large changes.
- Before changing code, check how the current files are organized.
- If something is unclear, check `/docs` first.

## Coding Rules

- Use Python as the main programming language.
- Use Tkinter for the desktop user interface.
- Use SQLite for local data storage.
- Keep code readable and suitable for a student course project.
- Use clear names for files, classes, functions, and variables.
- Keep comments short and useful.
- Avoid overcomplicated solutions.
- Test important changes before suggesting that the task is finished.

## Project Features

The AI assistant may help implement or improve:

- game settings: number of questions and difficulty mode;
- lifelines: 50/50 and Second Chance;
- game history saved in SQLite;
- leaderboard with best results;
- improved interface design;
- CSV import and export for questions;
- basic tests and bug fixes;
- documentation updates.

## Human and AI Responsibilities

The human developer is responsible for:

- final architecture decisions;
- checking course requirements;
- reviewing generated code;
- testing the final application;
- deciding which features are accepted.

AI assistants may help with:

- boilerplate code;
- small functions;
- refactoring;
- unit tests;
- documentation drafts;
- finding possible bugs;
- explaining code changes.

AI assistants must not:

- change the main architecture without approval;
- delete important files;
- add features not connected to the roadmap;
- ignore README.md and `/docs`;
- make the project too complex for the course level.


## Course checkpoint reminder (H1–H6)

- This repository starts from an inherited Part I baseline. Preserve the original repository history and baseline revision.
- Complete Exercise 1 onboarding, then H1 (review/architecture/baseline) before implementing the H2 feature.
- H2 delivers a bounded usable increment; H3 verifies and tags an early release; H4 improves it using H3 feedback and checks state/compatibility; H5 releases and *executes* rollback and fresh-target restore; H6 makes a small post-release patch and verifies handover and safe test-target retirement.
- For **every** assignment, each of the four humans needs an attributable contribution, substantive review of someone else's work, independent verification and short explanation. AI cannot act as a human reviewer.
- Maintain real evidence links to issues, PRs, reviews, test commands/results, CI and checkpoint SHAs under `docs/evidence/H1.md` ... `H6.md` as those assignments are performed. Never invent or mark evidence as complete before it exists.
- Local runtime data lives in ignored `MillionaireQuiz_Folder/local_data/`; don't change the tracked sample DB without an agreed and reviewed requirement.

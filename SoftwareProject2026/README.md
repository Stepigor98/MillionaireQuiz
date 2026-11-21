# Millionaire Quiz — Part I baseline

Millionaire Quiz is a desktop game built using **Python, Tkinter, and SQLite**.
It is the existing Part I project that will be developed in the H1–H6 course stages.
This baseline is intentionally **not** a new course feature.

## Existing working features

- Enter a player name and play 10 quiz questions (3 easy, 3 medium, 3 hard, 1 expert).
- Each question has four options and one correct answer.
- Win prizes for correct answers; take the money from €100 onward or lose on a wrong answer.
- Manage questions (add, edit, delete, search and filter by difficulty/category).
- View question counts by difficulty and category.

The separate `MillionaireQuiz_Folder/ui/lifeline_demo.py` is an **optional Streamlit demonstration** of the 50/50 strategy. The 50/50 button is **not yet integrated** into the Tkinter game.

## Run the main desktop application

**Requirements:** Python 3.10+ with the standard-library `tkinter` and `sqlite3` modules, and a graphical desktop session. No `pip install` is needed for the main game.

1. Download/extract this project or clone its Git repository.
2. On Windows, you can **double-click `START_HERE_WINDOWS.bat`** in the repository root. Alternatively, open a terminal inside `MillionaireQuiz_Folder`.
3. Launch the game:

   - Windows: `py main.py` (or `python main.py`)
   - macOS/Linux: `python3 main.py`

   Alternatively, from the repository root, use `python MillionaireQuiz_Folder/main.py` (or `python3` on your system).

4. Click **Start Game**, enter a player name and play. You can also open **Question Bank (Admin)** and **Statistics** from the main menu.

On some Linux distributions, Tkinter must be installed using your system package manager (for example, `python3-tk` on Debian/Ubuntu). The main game needs an active graphical display.

## Database — important for all four developers

- **Sample questions:** `MillionaireQuiz_Folder/data/quiz.db` (47 existing questions) are preserved as the **original read-only-by-convention sample**, tracked in Git.
- **Your local writable copy:** on first launch, the app copies it to `MillionaireQuiz_Folder/local_data/quiz.db`.
- Each teammate gets their own local writable file. `local_data/` is excluded by `.gitignore`, so personal test edits cannot accidentally modify the shared sample.
- To reset your local questions, close the application, back up anything important, then delete **only** `local_data/quiz.db`; it will be recreated from the sample on the next launch.
- For isolated testing, set `MILLIONAIRE_DB_PATH` to a disposable database path before starting the app.

No production passwords, API keys or personal data are required. Do not commit local databases, credentials or private files.

## Baseline checks

From the repository root, run standard-library unit tests:

```bash
python -m unittest discover -s tests -v
```

Optional GUI smoke test (opens an actual Tkinter window, uses a temporary database):

```bash
python tests/gui_smoke.py
```

On Linux without a physical display you can use `xvfb-run -a python tests/gui_smoke.py` if Xvfb is installed. The GUI smoke test runs through game, admin, and statistics paths without altering the sample database.

## Optional 50/50 Streamlit demonstration

Only for the separate Streamlit demo (not needed for the desktop game):

```bash
python -m pip install -r requirements.txt
streamlit run MillionaireQuiz_Folder/ui/lifeline_demo.py
```

## GitHub and course requirements

This ZIP includes files but **not prior Git commit history**. If the existing Part I project already has a GitHub repository, preserve that repository and apply changes there; do not replace it with a new unrelated history.

For H1, record the original repository URL and baseline SHA, inherited features and existing issues, create one small scope/contract decision and obtain an independent human baseline check. Later stages H2–H6 use that evidence; do not claim they are complete now. The instructor must have access to issues, pull requests, reviews, check runs and releases, even if the repository is private.

Planning and historical documentation: `docs/` and `AGENTS.md`. Future roadmap items are proposals, not features already delivered.

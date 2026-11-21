"""Exercise Tkinter in an actual display with temporary data (no dialogs)."""

import os
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "MillionaireQuiz_Folder"))


def exercise_app():
    from app import App
    from data import db

    app = App()
    try:
        app.withdraw()  # All GUI controls exist; avoid covering the desktop during smoke.
        app.update_idletasks()
        assert set(app.frames) == {
            "MainMenu", "StartGame", "GameScreen", "ResultScreen", "QuestionBank", "QuestionForm", "Statistics"
        }

        app.show("StartGame")
        start = app.frames["StartGame"]
        start.name_var.set("Smoke test")
        start.start()
        game = app.frames["GameScreen"]
        assert len(game.game_questions) == 10
        assert app.current_index == 0
        # Three correct answers unlock taking the money.
        for _ in range(3):
            q = game.game_questions[app.current_index]
            game.choose(q["correct"])
        assert app.current_win == 100 and app.current_index == 3
        assert str(game.take_btn["state"]) == "normal"
        game.take_money()
        assert "€100" in app.frames["ResultScreen"].msg_lbl["text"]

        # Wrong answer loses winnings, then a fresh run can win the game.
        app.reset_game()
        app.show("GameScreen")
        q = game.game_questions[0]
        game.choose((q["correct"] + 1) % 4)
        assert app.current_win == 0
        assert "Wrong answer" in app.frames["ResultScreen"].msg_lbl["text"]
        app.reset_game()
        app.show("GameScreen")
        for _ in range(10):
            q = game.game_questions[app.current_index]
            game.choose(q["correct"])
        assert app.current_win == 1_000_000
        assert "Congratulations" in app.frames["ResultScreen"].msg_lbl["text"]

        # Administrative and statistics screens use the same isolated real DB.
        app.show("Statistics")
        stats = app.frames["Statistics"]
        assert "47" in str(stats.total_lbl["text"])
        app.show("QuestionBank")
        bank = app.frames["QuestionBank"]
        assert len(bank.tree.get_children()) == 47
        bank.add()
        form = app.frames["QuestionForm"]
        form.text_var.set("GUI smoke question")
        for var, value in zip(form.opt_vars, ["A", "B", "C", "D"]):
            var.set(value)
        form.correct_var.set(2)
        form.level_var.set("easy")
        form.category_var.set("Smoke")
        form.save()
        assert db.total_questions() == 48
        match = db.list_questions("GUI smoke question")[0]
        qid = match["id"]
        bank.tree.selection_set(bank.tree.get_children()[0])
        bank.edit()
        form.text_var.set("GUI smoke edited")
        form.save()
        assert db.get_question_by_id(qid)["text"] == "GUI smoke edited"
        bank.tree.selection_set(bank.tree.get_children()[0])
        with patch("screens.question_bank.messagebox.askyesno", return_value=True):
            bank.delete()
        assert db.total_questions() == 47
        print("GUI smoke PASS: start / answers / take money / loss / win / admin CRUD / statistics")
    finally:
        app.destroy()


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        os.environ["MILLIONAIRE_DB_PATH"] = str(Path(d) / "quiz.db")
        exercise_app()

"""Baseline checks: run without a GUI or third-party packages."""

import hashlib
import sqlite3
import sys
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

GAME_DIR = Path(__file__).resolve().parents[1] / "MillionaireQuiz_Folder"
sys.path.insert(0, str(GAME_DIR))

from data import db  # noqa: E402
from lifelines.strategies import FiftyFiftyStrategy, LifelineContext  # noqa: E402


class DatabaseBaselineTests(unittest.TestCase):
    def setUp(self):
        self.work_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.work_dir.cleanup)
        self.db_path = Path(self.work_dir.name) / "nested" / "quiz.db"
        self.path_patch = patch.object(db, "DB_PATH", self.db_path)
        self.path_patch.start()
        self.addCleanup(self.path_patch.stop)
        self.sample_hash = hashlib.sha256(db.SAMPLE_DB_PATH.read_bytes()).hexdigest()
        db.init_db()

    def tearDown(self):
        self.assertEqual(
            hashlib.sha256(db.SAMPLE_DB_PATH.read_bytes()).hexdigest(),
            self.sample_hash,
            "Running tests must not modify the bundled sample DB",
        )

    def test_first_launch_copies_valid_baseline_database(self):
        self.assertTrue(self.db_path.is_file())
        self.assertNotEqual(self.db_path.resolve(), db.SAMPLE_DB_PATH.resolve())
        with closing(sqlite3.connect(self.db_path)) as conn:
            self.assertEqual(conn.execute("PRAGMA integrity_check").fetchone()[0], "ok")
        self.assertEqual(db.total_questions(), 47)
        self.assertEqual(sum(count for _, count in db.stats_questions_by_level()), 47)

    def test_game_selects_ten_questions_in_expected_difficulty_order(self):
        questions = db.fetch_game_questions()
        self.assertEqual(len(questions), 10)
        self.assertEqual([q["level"] for q in questions], ["easy"]*3 + ["medium"]*3 + ["hard"]*3 + ["expert"])
        for question in questions:
            self.assertEqual(len(question["options"]), 4)
            self.assertIn(question["correct"], range(4))
            self.assertTrue(question["text"])

    def test_question_bank_add_edit_filter_delete(self):
        before = db.total_questions()
        db.add_question(
            "Baseline test question?",
            ["Red", "Blue", "Green", "Yellow"],
            1, "easy", "TestCategory",
        )
        self.assertEqual(db.total_questions(), before + 1)
        matches = db.list_questions("baseline test", "easy", "TestCategory")
        self.assertEqual(len(matches), 1)
        qid = matches[0]["id"]
        self.assertEqual(db.get_question_by_id(qid)["options"][1], "Blue")
        db.update_question(
            qid, "Edited baseline question?",
            ["One", "Two", "Three", "Four"],
            3, "medium", "TestCategory",
        )
        self.assertEqual(db.get_question_by_id(qid)["correct"], 3)
        self.assertEqual(len(db.list_questions("edited baseline", "medium", "TestCategory")), 1)
        db.delete_question(qid)
        self.assertIsNone(db.get_question_by_id(qid))
        self.assertEqual(db.total_questions(), before)

    def test_missing_difficulty_is_an_explicit_error(self):
        db._exec("DELETE FROM questions WHERE level = ?", ("expert",))
        with self.assertRaisesRegex(ValueError, "Not enough questions"):
            db.fetch_game_questions()

    def test_init_db_does_not_reset_existing_local_edits(self):
        db.add_question("Preserve local?", ["A", "B", "C", "D"], 2, "hard", "Local")
        db.init_db()
        self.assertEqual(len(db.list_questions("Preserve local?")), 1)


class LifelineBaselineTests(unittest.TestCase):
    def setUp(self):
        self.context = LifelineContext(FiftyFiftyStrategy())
        self.options = ["Berlin", "Paris", "Rome", "Madrid"]

    def test_5050_uses_once_and_keeps_correct_answer(self):
        first = self.context.use_lifeline(self.options, "Paris", True)
        self.assertEqual(len(first["visible_options"]), 2)
        self.assertIn("Paris", first["visible_options"])
        self.assertFalse(first["lifeline_available"])
        second = self.context.use_lifeline(self.options, "Paris", False)
        self.assertEqual(second["visible_options"], self.options)
        self.assertFalse(second["lifeline_available"])

    def test_5050_rejects_invalid_question_without_using_lifeline(self):
        result = self.context.use_lifeline(self.options, "London", True)
        self.assertEqual(result["message"], "Invalid question data.")
        self.assertTrue(result["lifeline_available"])


if __name__ == "__main__":
    unittest.main()

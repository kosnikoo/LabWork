import sqlite3
import unittest
from src.database import DatabaseRepository


class DatabaseRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseRepository(":memory:")

    def tearDown(self):
        self.db.close()

    def test_add_success(self):
        self.assertTrue(self.db.add(1, "alice", "hello"))
        self.assertEqual(self.db.get_by_id(1)["name"], "alice")

    def test_add_duplicate_id_raises(self):
        self.db.add(1, "alice", "hello")
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.add(1, "bob", "again")

    def test_get_by_id_existing(self):
        self.db.add(2, "alice", "text")
        self.assertEqual(self.db.get_by_id(2)["message"], "text")

    def test_get_by_id_missing(self):
        self.assertIsNone(self.db.get_by_id(999))

    def test_get_by_name_returns_all(self):
        self.db.add(2, "alice", "a")
        self.db.add(1, "alice", "b")
        self.assertEqual([x["id"] for x in self.db.get_by_name("alice")], [1, 2])

    def test_get_by_name_missing_returns_empty(self):
        self.assertEqual(self.db.get_by_name("nobody"), [])

    def test_update_existing(self):
        self.db.add(3, "alice", "old")
        self.assertTrue(self.db.update(3, "new"))
        self.assertEqual(self.db.get_by_id(3)["message"], "new")

    def test_update_missing(self):
        self.assertFalse(self.db.update(404, "new"))

    def test_delete_existing(self):
        self.db.add(4, "alice", "remove")
        self.assertTrue(self.db.delete(4))
        self.assertIsNone(self.db.get_by_id(4))

    def test_delete_missing(self):
        self.assertFalse(self.db.delete(404))

    def test_validation(self):
        with self.assertRaises(ValueError):
            self.db.add(5, "", "message")
        with self.assertRaises(TypeError):
            self.db.add("5", "alice", "message")


if __name__ == "__main__":
    unittest.main()

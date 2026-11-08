import unittest
from src.database import DatabaseRepository
from src.parser import ForumParser

class ForumParserTest(unittest.TestCase):

    def test_parse_site_extracts_posts(self):
        data = ForumParser().parse_page("https://python.su/forum/topic/43600/")
        self.assertGreater(len(data), 0)
        self.assertEqual(set(data[0]), {"id", "name", "message"})
        self.assertIsInstance(data[0]["id"], int)
        self.assertTrue(data[0]["name"])
        self.assertTrue(data[0]["message"])

    def test_parse_site_finds_known_post(self):
        data = ForumParser().parse_page("https://python.su/forum/topic/43600/")
        self.assertTrue(any(post["id"] == 231390 for post in data))

    def test_save_to_db(self):
        repository = DatabaseRepository(":memory:")
        count = ForumParser().save_to_db(
            [{"id": 1, "name": "alice", "message": "Hi"}], repository
        )
        self.assertEqual(count, 1)
        self.assertEqual(repository.get_by_id(1)["name"], "alice")
        repository.close()


if __name__ == "__main__":
    unittest.main()

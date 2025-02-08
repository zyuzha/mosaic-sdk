import unittest
from mosaic.community import NetworkAPI
from mosaic.rating import RatingAPI

class TestRatingAPI(unittest.TestCase):
    def setUp(self):
        self.network_api = NetworkAPI()
        self.rating_api = RatingAPI(self.network_api._community_data)
        self.network_api.share_knowledge("Learn Python")

    def test_rate_knowledge(self):
        self.rating_api.rate_knowledge("Learn Python", 5)
        self.assertEqual(self.rating_api.ratings["Learn Python"], [5])

    def test_get_average_rating(self):
        self.rating_api.rate_knowledge("Learn Python", 5)
        self.rating_api.rate_knowledge("Learn Python", 3)
        average_rating = self.rating_api.get_average_rating("Learn Python")
        self.assertEqual(average_rating, 4.0)

    def test_rate_knowledge_invalid(self):
        with self.assertRaises(TypeError):
            self.rating_api.rate_knowledge(123, 5)
        with self.assertRaises(TypeError):
            self.rating_api.rate_knowledge("Learn Python", "five")
        with self.assertRaises(ValueError):
            self.rating_api.rate_knowledge("Learn Python", 6)
        with self.assertRaises(ValueError):
            self.rating_api.rate_knowledge("Unknown Knowledge", 5)

    def test_get_average_rating_invalid(self):
        with self.assertRaises(TypeError):
            self.rating_api.get_average_rating(123)
        with self.assertRaises(ValueError):
            self.rating_api.get_average_rating("Unknown Knowledge")

if __name__ == '__main__':
    unittest.main()
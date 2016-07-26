import unittest

from application.occupancy_prediction import set_occupancy_category

class Testing(unittest.TestCase):
    def test_set_occupancy_category(self):
        assert (set_occupancy_category(0, 5) == (0, "empty", False))
        assert (set_occupancy_category(1, 5) == (0.25, "moderate", True))
        assert (set_occupancy_category(2, 5) == (0.5, "moderate", True))
        assert (set_occupancy_category(3, 5) == (0.5, "moderate", True))
        assert (set_occupancy_category(4, 5) == (0.75, "full", True))
        assert (set_occupancy_category(5, 5) == (1.0, "full", True))
        assert (set_occupancy_category(6, 5) == (1.0, "full", True))


if __name__ == '__main__':
    unittest.main()
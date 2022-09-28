import unittest
from app import paint_needed


class TestPaintArea(unittest.TestCase):
    def test_paint(self):  # Test paint area when total area >= 0.
        self.assertAlmostEqual(paint_needed(1), 0.1)
        self.assertAlmostEqual(paint_needed(0), 0)
        self.assertAlmostEqual(paint_needed(1.5), 0.15)


if __name__ == '__main__':
    unittest.main()

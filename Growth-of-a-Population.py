import unittest
import math


# CodeWars
def nb_year(p0, percent, aug, p):
    inhabitants = p0
    count = 0
    while inhabitants < p:
        inhabitants += inhabitants * percent / 100 + aug
        count += 1
    return count


class TestRemoveChar(unittest.TestCase):
    def test(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)


if __name__ == '__main__':
    unittest.main()

import unittest


# CodeWars
def unique_in_order(iterable):
    unique = list()
    for item in iterable:
        if not unique or item != unique[-1]:
            unique.append(item)
    return unique


class TestUniqueInOrder(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])
        self.assertEqual(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()

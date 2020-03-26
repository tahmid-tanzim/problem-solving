import unittest


# CodeWars
def get_middle(s):
    n = len(s)
    m = n // 2
    return s[m - 1:m + 1] if n % 2 == 0 else s[m:m + 1]


class TestRemoveChar(unittest.TestCase):
    def test(self):
        self.assertEqual(get_middle("test"), "es")
        self.assertEqual(get_middle("testing"), "t")
        self.assertEqual(get_middle("middle"), "dd")
        self.assertEqual(get_middle("A"), "A")
        self.assertEqual(get_middle("of"), "of")


if __name__ == '__main__':
    unittest.main()

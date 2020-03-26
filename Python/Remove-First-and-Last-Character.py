import unittest


# CodeWars
def remove_char(s):
    return s[1:-1]


class TestRemoveChar(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_char('eloquent'), 'loquen')
        self.assertEqual(remove_char('country'), 'ountr')
        self.assertEqual(remove_char('person'), 'erso')
        self.assertEqual(remove_char('place'), 'lac')
        self.assertEqual(remove_char('ok'), '')


if __name__ == '__main__':
    unittest.main()

import unittest


# CodeWars
def solution(number):
    sum = 0
    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


class TestRemoveChar(unittest.TestCase):
    def test(self):
        self.assertEqual(solution(12), 23)


if __name__ == '__main__':
    unittest.main()

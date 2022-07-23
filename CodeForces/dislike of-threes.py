# https://codeforces.com/problemset/problem/1560/A
# A. Dislike of Threes


def getPolycarpSequence(k: int) -> int:
    value = 0
    for _ in range(k):
        value += 1
        while value % 3 == 0 or value % 10 == 3:
            value += 1
    return value


if __name__ == "__main__":
    for t in range(int(input())):
        print(getPolycarpSequence(int(input())))

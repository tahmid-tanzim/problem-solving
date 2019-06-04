# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/mojtaba-prepares-contest-29b2a044/


if __name__ == '__main__':
    T = int(input())
    min_cost = []
    while T > 0:
        G, P = [int(x) for x in input().split()]
        n = int(input())
        c1, c2 = 0, 0
        while n > 0:
            i, j = [int(x) for x in input().split()]
            c1 += G * i + P * j
            c2 += G * j + P * i
            n -= 1
        min_cost.append(min(c1, c2))
        T -= 1

    for c in min_cost:
        print(c)


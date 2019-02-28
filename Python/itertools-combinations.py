from itertools import combinations

if __name__ == '__main__':
    S, k = input().split()
    for x in range(1, int(k) + 1):
        t = sorted([''.join(sorted(i)) for i in combinations(S, x)])
        print(*t, sep="\n")

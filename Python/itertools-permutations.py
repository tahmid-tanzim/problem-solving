from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()
    t = sorted([''.join(i) for i in permutations(S, int(k))])
    print(*t, sep="\n")

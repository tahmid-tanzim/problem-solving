from itertools import combinations_with_replacement

if __name__ == '__main__':
    S, k = input().split()
    t = sorted([''.join(sorted(i)) for i in combinations_with_replacement(S, int(k))])
    print(*t, sep="\n")

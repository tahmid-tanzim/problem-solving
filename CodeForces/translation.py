# https://codeforces.com/problemset/problem/41/A
# A. Translation

def isTranslatable(t: str, s: str) -> str:
    j = len(s)
    if len(t) != j:
        return 'NO'
    j -= 1
    i = 0
    while j >= 0:
        if t[i] != s[j]:
            return 'NO'
        i += 1
        j -= 1
    return 'YES'


if __name__ == "__main__":
    print(isTranslatable(input(), input()))

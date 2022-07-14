# https://codeforces.com/problemset/problem/236/A
# A. Boy or Girl

if __name__ == "__main__":
    charSet = set(c for c in input())
    print("CHAT WITH HER!" if len(charSet) % 2 == 0 else "IGNORE HIM!")


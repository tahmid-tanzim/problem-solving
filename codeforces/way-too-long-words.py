# https://codeforces.com/problemset/problem/71/A
# A. Way Too Long Words
if __name__ == "__main__":
    for _ in range(int(input())):
        word = input()
        n = len(word)
        if n > 10:
            print(f"{word[0]}{n - 2}{word[n - 1]}")
        else:
            print(word)

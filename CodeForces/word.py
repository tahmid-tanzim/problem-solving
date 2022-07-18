# https://codeforces.com/problemset/problem/59/A
# A. Word

if __name__ == "__main__":
    word = input()
    count = {
        'uppercase': 0,
        'lowercase': 0,
    }

    for char in word:
        if ord(char) >= 97:
            count['lowercase'] += 1
        else:
            count['uppercase'] += 1

    if count['uppercase'] > count['lowercase']:
        print(word.upper())
    else:
        print(word.lower())

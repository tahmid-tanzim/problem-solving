# https://codeforces.com/problemset/problem/96/A
# A. Football


if __name__ == "__main__":
    result = 'NO'
    currentPlayer = '-1'
    count = 0
    for i in input():
        if currentPlayer != i:
            currentPlayer = i
            count = 1
        else:
            count += 1

        if count >= 7:
            result = 'YES'
            break

    print(result)

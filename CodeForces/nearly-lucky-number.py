# https://codeforces.com/problemset/problem/110/A
# A. Nearly Lucky Number

if __name__ == "__main__":
    number = int(input())
    count = 0
    while number > 0:
        digit = number % 10
        if digit == 4 or digit == 7:
            count += 1
        number //= 10
    print('YES' if count == 4 or count == 7 else 'NO')


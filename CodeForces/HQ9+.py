# https://codeforces.com/problemset/problem/133/A
# A. HQ9+

if __name__ == "__main__":
    result = 'NO'
    for char in input():
        ASCII_VALUE = ord(char)
        if ASCII_VALUE == 72 or ASCII_VALUE == 81 or ASCII_VALUE == 57:
            result = 'YES'
            break
    print(result)

    

# https://codeforces.com/problemset/problem/112/A
# A. Petya and Strings

if __name__ == "__main__":
    string1 = input()
    string2 = input()
    result = 0
    for i in range(len(string1)):
        asciiValue1 = ord(string1[i])
        asciiValue2 = ord(string2[i])

        if asciiValue1 >= 97:
            asciiValue1 -= 32
        if asciiValue2 >= 97:
            asciiValue2 -= 32
        
        if asciiValue1 < asciiValue2:
            result = -1
            break
        elif asciiValue1 > asciiValue2:
            result = 1
            break
    print(result)

    

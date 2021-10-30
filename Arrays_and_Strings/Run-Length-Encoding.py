#!/usr/bin/python3
# https://www.algoexpert.io/questions/Run-Length%20Encoding


def encodeStr(count, c):
    encode = str()
    remainder = count - 9
    while remainder > 0:
        encode += f'9{c}'
        count = remainder
        remainder -= 9
    encode += f'{count}{c}'
    return encode


# O(n) time, O(n) space
def runLengthEncoding(string):
    frequency = list(string)
    output = ""
    c = frequency[0]
    i = 1
    count = 1
    while i < len(frequency):
        if c == frequency[i]:
            count += 1
        else:
            output += encodeStr(count, c)
            c = frequency[i]
            count = 1
        i += 1
    output += encodeStr(count, c)
    return output


if __name__ == '__main__':
    print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))  # "9A4A2B4C2D"

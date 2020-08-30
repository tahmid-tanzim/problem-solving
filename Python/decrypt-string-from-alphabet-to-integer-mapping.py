#!/usr/local/bin/python3
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/


def freq_alphabets(s):
    i = len(s) - 1
    output = ''
    while i >= 0:
        if s[i] == '#':
            ascii_code = int(s[i-2:i]) + 96
            i -= 3
        else:
            ascii_code = int(s[i]) + 96
            i -= 1
        output = chr(ascii_code) + output
    return output


if __name__ == '__main__':
    print(freq_alphabets("10#11#12"))  # 'jkab'
    print(freq_alphabets("1326#"))  # 'acz'
    print(freq_alphabets("25#"))  # 'y'
    print(freq_alphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))

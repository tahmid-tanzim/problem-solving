#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/to-lower-case/


def to_lower_case(str):
    output = []
    for c in str:
        ASCII_DEC = ord(c)
        output.append(chr(ASCII_DEC + 32) if ASCII_DEC >= 65 and ASCII_DEC <= 90 else c)
    return ''.join(output)


if __name__ == '__main__':
    print(to_lower_case('Lorem Ipsum TAHMID TaNzIm'))


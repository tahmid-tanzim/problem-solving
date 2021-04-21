#!/usr/bin/python3
# Cracking the Coding Interview - 1.3
from typing import List


def replaceSpaces(string: List[str], trueLength: int) -> List[str]:
    spaceCount = 0
    for i in range(trueLength):
        if string[i] == ' ':
            spaceCount += 1

    index = trueLength + spaceCount * 2
    del string[index:]

    for i in range(trueLength - 1, -1, -1):
        if string[i] == ' ':
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
    return string


def replaceSpacesFromString(string: str, trueLength: int) -> str:
    spaceCount = 0
    for i in range(trueLength):
        if string[i] == ' ':
            spaceCount += 1

    index = trueLength + spaceCount * 2
    string = string[:index]

    for i in range(trueLength - 1, -1, -1):
        if string[i] == ' ':
            string = string[:index - 3] + '%20' + string[index:]
            index -= 3
        else:
            string = string[:index - 1] + string[i] + string[index:]
            index -= 1
    return string


if __name__ == '__main__':
    # output = replaceSpaces(list("Mr John Smith       "), 13)
    output = replaceSpacesFromString("Mr John Smith       ", 13)
    print(f'{output}')

#!/usr/bin/python3
# https://www.algoexpert.io/questions/First%20Non-Repeating%20Character


def firstNonRepeatingCharacter(string):
    hashtable = dict()
    index = 0
    for char in string:
        if char in hashtable:
            hashtable[char][0] += 1
        else:
            hashtable[char] = [1, index]
        index += 1

    for key in hashtable:
        if hashtable[key][0] == 1:
            print(f'First Non-Repeating Character is {key} at index {hashtable[key][1]}')
            return hashtable[key][1]

    return -1


if __name__ == '__main__':
    print(f'Answer - {firstNonRepeatingCharacter("abcdcafcbdf")}')

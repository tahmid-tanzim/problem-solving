#!/usr/bin/python3
# Cracking the Coding Interview - 1.2

def permutation(s: str, t: str):
    """
    Case Sensitive
    Time - O(n)
    Space - O(1)
    """
    if len(s) != len(t):
        return False

    letters = [0] * 128
    for i in s:
        letters[ord(i)] += 1

    for i in t:
        if letters[ord(i)] == 0:
            return False
        letters[ord(i)] -= 1
    return True


def checkPermutation(s: str, t: str):
    """
    Case Insensitive & Discard Space
    i.e. Allow "  God  " == "dog"
    Time - O(n)
    Space - O(1)
    """
    hashtable = dict()
    for i in s:
        if i == ' ':
            continue

        i = i.upper()
        if i in hashtable:
            hashtable[i] += 1
        else:
            hashtable[i] = 1

    for i in t:
        if i == ' ':
            continue

        i = i.upper()
        if i not in hashtable or hashtable[i] == 0:
            return False

        hashtable[i] -= 1

    return True


if __name__ == '__main__':
    output1 = permutation("god", "dog")
    print(f'output1 - {output1}')

    output2 = checkPermutation("  God   ", "dog")
    print(f'output2 - {output2}')


#!/usr/bin/python3
# https://www.algoexpert.io/questions/Phone%20Number%20Mnemonics
"""
If you open the keypad of your mobile phone, it'll likely look like this:
   ----- ----- -----
  |     |     |     |
  |  1  |  2  |  3  |
  |     | abc | def |
   ----- ----- -----
  |     |     |     |
  |  4  |  5  |  6  |
  | ghi | jkl | mno |
   ----- ----- -----
  |     |     |     |
  |  7  |  8  |  9  |
  | pqrs| tuv | wxyz|
   ----- ----- -----
        |     |
        |  0  |
        |     |
         -----

  Almost every digit is associated with some letters in the alphabet; this
  allows certain phone numbers to spell out actual words. For example, the phone
  number 8464747328 can be written as timisgreat;
  similarly, the phone number 2686463 can be written as
  antoine or as ant6463.

  It's important to note that a phone number doesn't represent a single sequence
  of letters, but rather multiple combinations of letters. For instance, the
  digit 2 can represent three different letters (a, b, and c).

  A mnemonic is defined as a pattern of letters, ideas, or associations that
  assist in remembering something. Companies oftentimes use a mnemonic for their
  phone number to make it easier to remember.

  Given a stringified phone number of any non-zero length, write a function that
  returns all mnemonics for this phone number, in any order.

  For this problem, a valid mnemonic may only contain letters and the digits
  0 and 1. In other words, if a digit is able to be
  represented by a letter, then it must be. Digits 0 and
  1 are the only two digits that don't have letter representations
  on the keypad.

  Note that you should rely on the keypad illustrated above for digit-letter
  associations.

Sample Input
phoneNumber = "1905"

Sample Output
[
  "1w0j",
  "1w0k",
  "1w0l",
  "1x0j",
  "1x0k",
  "1x0l",
  "1y0j",
  "1y0k",
  "1y0l",
  "1z0j",
  "1z0k",
  "1z0l",
]
// The mnemonics could be ordered differently.
"""


# O(4^n * n) time | O(4^n * n) space
# where n is the length of the phone number
class Solution1:
    # Iterative Solution
    @staticmethod
    def phoneNumberMnemonics(phoneNumber):
        keypad = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        mnemonic = ['']

        for digit in phoneNumber:
            keypad_letters = keypad[int(digit)]
            i = 0
            n = len(mnemonic)
            while i < n:
                item = mnemonic.pop(0)
                for letter in keypad_letters:
                    mnemonic.append(item + letter)
                i += 1

        return mnemonic


class Solution2:
    # Recursive Solution
    def __init__(self):
        self.KEYPAD = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def phoneNumberMnemonicsHelper(self, idx, phoneNumber, currentMnemonics, mnemonicsFound):
        if idx == len(phoneNumber):
            mnemonicsFound.append("".join(currentMnemonics))
            return

        digit = phoneNumber[idx]
        keypad_letters = self.KEYPAD[int(digit)]
        for letter in keypad_letters:
            currentMnemonics[idx] = letter
            self.phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonics, mnemonicsFound)

    def phoneNumberMnemonics(self, phoneNumber):
        currentMnemonics = [0] * len(phoneNumber)
        mnemonicsFound = []
        self.phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonics, mnemonicsFound)
        return mnemonicsFound


if __name__ == "__main__":
    s1 = Solution1()
    print(f'Output - {s1.phoneNumberMnemonics("1905")}')
    s2 = Solution2()
    print(f'Output - {s2.phoneNumberMnemonics("1905")}')


#!/usr/bin/python3
# https://www.algoexpert.io/questions/Balanced%20Brackets
"""
  Write a function that takes in a string made up of brackets ((,
  [, {, ), ], and
  }) and other optional characters. The function should return a
  boolean representing whether the string is balanced with regards to brackets.

  A string is said to be balanced if it has as many opening brackets of a
  certain type as it has closing brackets of that type and if no bracket is
  unmatched. Note that an opening bracket can't match a corresponding closing
  bracket that comes before it, and similarly, a closing bracket can't match a
  corresponding opening bracket that comes after it. Also, brackets can't
  overlap each other as in
  [(]).

Sample Input
string = "([])(){}(())()()"

Sample Output
true // it's balanced
"""


# O(n) time, O(n) space
def balancedBrackets(string):
    stack = []
    for s in string:
        if s in '({[':
            stack.append(s)
            continue
        if s not in ')}]':
            continue
        if len(stack) == 0 or (
                stack[-1] == '(' and s != ')' or stack[-1] == '{' and s != '}' or stack[-1] == '[' and s != ']'):
            return False
        stack.pop(-1)
    return len(stack) == 0


if __name__ == "__main__":
    print(balancedBrackets("([])(){}(())()()"))

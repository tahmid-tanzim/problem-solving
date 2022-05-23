#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/


# Time O(n)
# Space O(n)
def findBrackets(S: str) -> int:
    stack = []
    for char in S:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
            continue

        if len(stack) == 0:
            return 0
        else:
            last_char = stack.pop()
            if (char == ")" and last_char != "(") or \
                    (char == "}" and last_char != "{") or \
                    (char == "]" and last_char != "["):
                return 0
    return 1 if len(stack) == 0 else 0


# Time O(n)
# Space O(n)
def findBrackets2(S: str) -> int:
    stack = []
    for char in S:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)
            continue

        try:
            last_char = stack.pop()
            if (char == ")" and last_char != "(") or \
                    (char == "}" and last_char != "{") or \
                    (char == "]" and last_char != "["):
                return 0
        except IndexError:
            return 0
    return 1 if len(stack) == 0 else 0


if __name__ == '__main__':
    inputs = (
        {
            "S": "{[()()]}",
            "expected": 1
        },
        {
            "S": "([)()]",
            "expected": 0
        },
        {
            "S": "{}]",
            "expected": 0
        },
        {
            "S": "{{{{",
            "expected": 0
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findBrackets(val["S"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")

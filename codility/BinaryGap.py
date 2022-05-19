#!/usr/bin/python3
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/


def findBinaryGap(n: int):
    max_gap = 0
    binary = str(bin(n))
    i = 2
    counter = 0
    found_start_one = False
    # print(n, binary)
    while i < len(binary):
        # print(n, i, binary[i])
        if binary[i] == '0' and found_start_one:
            counter += 1
        elif binary[i] == '1':
            if counter > max_gap:
                max_gap = counter
            counter = 0
            found_start_one = True
        i += 1
    return max_gap


if __name__ == '__main__':
    inputs = (
        {
            "N": 9,
            "expected": 2
        },
        {
            "N": 529,
            "expected": 4
        },
        {
            "N": 20,
            "expected": 1
        },
        {
            "N": 15,
            "expected": 0
        },
        {
            "N": 32,
            "expected": 0
        },
        {
            "N": 1,
            "expected": 0
        },
        {
            "N": 2147483647,
            "expected": 0
        },
        {
            "N": 2147483645,
            "expected": 1
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = findBinaryGap(val["N"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:{output:9}\nExpected:{val['expected']:7}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output:9}\nExpected:{val['expected']:7}\n")

    print(f"Passed: {test_passed:6}/{idx + 1}\n")

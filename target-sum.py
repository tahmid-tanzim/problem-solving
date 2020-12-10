#!/usr/local/bin/python3
# Code to Measure time taken by program to execute.
import time


def can_sum(numbers: list, target: int, memo: dict) -> bool:
    # Base Case
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if can_sum(numbers, remainder, memo):
            memo[target] = True
            return memo[target]

    memo[target] = False
    return memo[target]


if __name__ == "__main__":
    # store starting time
    begin = time.time()

    print(can_sum([2, 3], 7, {}))  # TRUE
    print(can_sum([5, 3, 4, 7], 7, {}))  # TRUE
    print(can_sum([2, 4], 7, {}))  # FALSE
    print(can_sum([2, 3, 5], 8, {}))  # TRUE
    print(can_sum([7, 14], 300, {}))  # FALSE

    # program body ends

    time.sleep(1)
    # store end time
    end = time.time()

    # total time taken
    print(f"Total runtime of the program is {end - begin}")

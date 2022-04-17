#!/usr/bin/python3
from typing import List

"""
Task 3 - 62%
An industrial company has N factories, each producing some pollution every month. 
The company has decided to reduce its total fume emissions by equipping some 
factories with one or more filters.
 
Every such filter reduces the pollution of a factory by half. 
When a second (or subsequent) filter is applied, it again reduces by half 
the remaining pollution emitted after fitting the existing filter(s). 
For example, a factory that initially produces 6 units of pollution will generate 3 units 
with one filter, 1.5 units with two filters and 0.75 units with three filters. 

You are given an array of N integers describing the amount of pollution produced by 
the factories. Your task is to find the minimum number of filters needed to decrease 
the total sum of pollution by at least half. 

Write a function: 
    def solution(A) 
    
which, given an array of integers A of length N, returns the minimum number of filters 
needed to reduce the total pollution by at least half. 

Examples: 
1. Given A = [5, 19, 8, 1], your function should return 3. 
The initial total pollution is 5 + 19 + 8 + 1 = 33. 
We install two filters at the factory producing 19 units and one filter at the factory
producing 8 units. Then the total pollution will be 
5 + (19/2)/2) + (8 / 2) + 1 = 5 + 4.75 + 4 + 1 = 14.75 
which is less than 33 / 2 = 16.5, so we have achieved our goal. 

2. Given A = [10, 10], your function should return 2, 
because we may install one filter at each factory. 

3. Given A = [3, 0, 5], your function should return 2, 
because it is sufficient to install one filter at each factory producing a non-zero amount 
of pollution. 

Write an efficient algorithm for the following assumptions: 

    - N is an integer within the range [1..30,000); 
    - each element of array A is an integer within the range (0...70,000).
"""


def findMinNumberOfFilter(A: List[int]) -> int:
    total_pollution = sum(A)
    required_pollution = total_pollution / 2
    filter_installed = 0
    while total_pollution > required_pollution:
        max_pollution = max(A)
        idx = A.index(max_pollution)

        max_pollution /= 2
        filter_installed += 1

        total_pollution -= max_pollution
        A[idx] = max_pollution

    return filter_installed


if __name__ == '__main__':
    inputs = (
        {
            "A": [5, 19, 8, 1],
            "expected": 3
        },
        {
            "A": [10, 10],
            "expected": 2
        },
        {
            "A": [3, 0, 5],
            "expected": 2
        },
    )

    test_passed = 0
    for i, val in enumerate(inputs):
        output = findMinNumberOfFilter(val["A"])
        if output == val['expected']:
            print(f"{i}. CORRECT Answer\nOutput:{output}\nExpected:{val['expected']}\n\n")
            test_passed += 1
        else:
            print(f"{i}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n\n")

    print(f"Passed - {test_passed}/{i + 1}")

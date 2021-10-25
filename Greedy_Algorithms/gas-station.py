#!/usr/bin/python3
# https://leetcode.com/problems/gas-station/
from typing import List


# Greedy Algorithms
# Time Complexity - O(n), `n` is number of cities.
# Space Complexity - O(1)
def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    numberOfGasStations = len(gas)
    gasRemaining = 0

    startingStation = 0
    minimumGasRemaining = 0

    for currentStation in range(1, numberOfGasStations):
        gasRemaining = gasRemaining + gas[currentStation - 1] - cost[currentStation - 1]

        if gasRemaining < minimumGasRemaining:
            minimumGasRemaining = gasRemaining
            startingStation = currentStation

    return -1 if gasRemaining + gas[-1] - cost[-1] < 0 else startingStation


if __name__ == "__main__":
    # output = canCompleteCircuit(
    #     [1, 2, 3, 4, 5],
    #     [3, 4, 5, 1, 2]
    # )

    output = canCompleteCircuit(
        [2, 3, 4],
        [3, 4, 3]
    )

    # output = validStartingCityGreedy(
    #     [5, 25, 15, 10, 15],
    #     [1, 2, 1, 0, 3],
    #     10
    # )

    print(output)

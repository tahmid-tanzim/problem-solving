#!/usr/bin/python3
# https://www.algoexpert.io/questions/Minimum%20Waiting%20Time
"""
Write a function that returns the minimum amount of total waiting time for all of the queries.
For example, if you're given the queries of durations [1, 4, 5],
then the total waiting time if the queries were executed in the order of [5, 1, 4] would be
(0) + (5) + (5 + 1) = 11.
The first query of duration 5 would be executed immediately,
so its waiting time would be 0,
the second query of duration 1 would have to wait 5 seconds (the duration of the first query) to be executed,
and the last query would have to wait the duration of the first two queries before being executed.
"""


# Time Complexity - O(nlog(n))
# Space Complexity - O(1)
def minimumWaitingTime(queries):
    queries.sort()
    waitingTime = 0
    total = 0
    for q in queries:
        waitingTime += total
        total += q
    return waitingTime


if __name__ == "__main__":
    output = minimumWaitingTime([3, 2, 1, 2, 6])  # 17
    print(output)

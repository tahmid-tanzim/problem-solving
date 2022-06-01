#!/usr/bin/python3
# https://www.algoexpert.io/questions/Topological%20Sort
"""
  You're given a list of arbitrary jobs that need to be completed; these jobs
  are represented by distinct integers. You're also given a list of dependencies. A
  dependency is represented as a pair of jobs where the first job is a
  prerequisite of the second one. In other words, the second job depends on the
  first one; it can only be completed once the first job is completed.

  Write a function that takes in a list of jobs and a list of dependencies and
  returns a list containing a valid order in which the given jobs can be
  completed. If no such order exists, the function should return an empty array.

Sample Input
jobs = [1, 2, 3, 4]
deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

Sample Output
[1, 4, 3, 2] or [4, 1, 3, 2]
"""


# O(j + d) time | O(j + d) space
# where j is the number of jobs and d is the number of dependencies
def topologicalSort(jobs, deps):
    adjacencyList = {j: [] for j in jobs}
    for prerequisiteJob, originalJob in deps:
        adjacencyList[originalJob].append(prerequisiteJob)

    visited = [False for _ in jobs]
    path = [False for _ in jobs]
    stack = []

    def isCycleExists(job: int):
        visited[job - 1] = True
        path[job - 1] = True

        for prereqJob in adjacencyList[job]:
            if not visited[prereqJob - 1]:
                if isCycleExists(prereqJob):
                    return True
            elif path[prereqJob - 1]:
                return True

        path[job - 1] = False
        stack.append(job)
        return False

    for j in jobs:
        if not visited[j - 1]:
            if isCycleExists(j):
                return []
    return stack


if __name__ == "__main__":
    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    print(topologicalSort(jobs, deps))

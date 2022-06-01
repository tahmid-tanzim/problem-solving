#!/usr/bin/python3
# https://leetcode.com/problems/course-schedule-ii/
from typing import List, Tuple
"""
Topological Sort
"""


class Solution:
    def __init__(self):
        self.adjacencyList: List[List[int]] = list()

    def isCyclicGraph(self, courseIdx: int, visited: List[bool], path: List[bool], result: List[int]) -> bool:
        visited[courseIdx] = True
        path[courseIdx] = True

        for prerequisiteCourse in self.adjacencyList[courseIdx]:
            if not visited[prerequisiteCourse]:
                if self.isCyclicGraph(prerequisiteCourse, visited, path, result):
                    # cycle found
                    return True
            elif path[prerequisiteCourse]:
                # visited previously - cycle found
                return True

        # No cycle found - return to parent call stack & courseIdx is fully visited
        path[courseIdx] = False
        result.append(courseIdx)
        return False

    def findOrder(self, numCourses: int, prerequisites: List[Tuple[int, int]]) -> List[int]:
        self.adjacencyList = [[] for _ in range(numCourses)]
        for courseNumber, prerequisiteCourseNumber in prerequisites:
            self.adjacencyList[courseNumber].append(prerequisiteCourseNumber)

        visited = [False for _ in range(numCourses)]  # visited list works as memoization
        path = [False for _ in range(numCourses)]  # used only inside DFS to check cycle
        result = []

        # DFS, depth first search
        for course in range(numCourses):
            if not visited[course]:
                if self.isCyclicGraph(course, visited, path, result):
                    return []

        return result


if __name__ == "__main__":
    inputs = (
        {
            "numCourses": 2,
            "prerequisites": [
                (1, 0,),
            ],
            "expected": [0, 1]
        },
        {
            "numCourses": 4,
            "prerequisites": [
                (1, 0,),
                (2, 0,),
                (3, 1,),
                (3, 2,),
            ],
            "expected": [0, 1, 2, 3]
        },
        {
            "numCourses": 1,
            "prerequisites": [],
            "expected": [0]
        },
        {
            "numCourses": 2,
            "prerequisites": [
                (0, 1,),
                (1, 0,),
            ],
            "expected": []
        },
    )

    test_passed = 0
    obj = Solution()
    for idx, val in enumerate(inputs):
        output = obj.findOrder(val["numCourses"], val["prerequisites"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:{output}\nExpected:{val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")

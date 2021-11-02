#!/usr/bin/python3
# https://www.algoexpert.io/questions/Min%20Rewards
"""
  Imagine that you're a teacher who's just graded the final exam in a class. You
  have a list of student scores on the final exam in a particular order (not
  necessarily sorted), and you want to reward your students. You decide to do so
  fairly by giving them arbitrary rewards following two rules:

  1. All students must receive at least one reward.
  
  2. Any given student must receive strictly more rewards than an adjacent
    student (a student immediately to the left or to the right) with a lower
    score and must receive strictly fewer rewards than an adjacent student with
    a higher score.

  Write a function that takes in a list of scores and returns the minimum number
  of rewards that you must give out to students to satisfy the two rules.

  You can assume that all students have different scores; in other words, the
  scores are all unique.

Sample Input
scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]

Sample Output
25 // you would give out the following rewards: [4, 3, 2, 1, 2, 3, 4, 5, 1]
"""


# Time - O(n) | Space O(n)
class Solution1:
    @staticmethod
    def minRewards(scores):
        n = len(scores)
        rewards = [1 for _ in range(n)]

        # Traverse from Left to Right
        i = 1
        while i < n:
            if scores[i - 1] < scores[i]:
                rewards[i] = rewards[i - 1] + 1
            i += 1

        # Traverse from Right to Left
        i = n - 2
        while i >= 0:
            if scores[i] > scores[i + 1]:
                rewards[i] = max(rewards[i], rewards[i + 1] + 1)
            i -= 1

        return sum(rewards)


# Time - O(n^2) | Space O(n)
class Solution2:
    @staticmethod
    def minRewards(scores):
        rewards = list()
        n = len(scores)
        min_index = -1
        min_value = float('inf')

        for i in range(n):
            rewards.insert(i, 0)
            if scores[i] < min_value:
                min_index = i
                min_value = scores[i]

        rewards[min_index] = 1

        # Left Traverse
        leftIdx = min_index - 1
        while leftIdx >= 0:
            if scores[leftIdx] > scores[leftIdx + 1]:
                rewards[leftIdx] = rewards[leftIdx + 1] + 1
            if scores[leftIdx] < scores[leftIdx + 1] and rewards[leftIdx + 1] == 1:
                rewards[leftIdx] = 1
                i = leftIdx + 1
                while i < n:
                    if scores[i - 1] > scores[i]:
                        break
                    rewards[i] += 1
                    i += 1
            if scores[leftIdx] < scores[leftIdx + 1] and rewards[leftIdx + 1] != 1:
                rewards[leftIdx] = 1
            # if scores[leftIdx + 1] == scores[leftIdx]:
            # 	rewards[leftIdx] = rewards[leftIdx + 1]
            leftIdx -= 1

        # Right Traverse
        rightIdx = min_index + 1
        while rightIdx < n:
            if scores[rightIdx - 1] < scores[rightIdx]:
                rewards[rightIdx] = rewards[rightIdx - 1] + 1
            if scores[rightIdx - 1] > scores[rightIdx] and rewards[rightIdx - 1] == 1:
                rewards[rightIdx] = 1
                i = rightIdx - 1
                while i >= 0:
                    if scores[i] < scores[i + 1]:
                        break
                    rewards[i] += 1
                    i -= 1
            if scores[rightIdx - 1] > scores[rightIdx] and rewards[rightIdx - 1] != 1:
                rewards[rightIdx] = 1
            # if scores[rightIdx - 1] == scores[rightIdx]:
            # 	rewards[rightIdx] = rewards[rightIdx - 1]
            rightIdx += 1

        return sum(rewards)


if __name__ == '__main__':
    obj = Solution1()
    print(f'{obj.minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5])}')
    obj = Solution2()
    print(f'{obj.minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5])}')

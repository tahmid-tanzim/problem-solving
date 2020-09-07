#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/contains-duplicate/
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

# def contains_duplicate(nums):
#     i = 0
#     mapper = {}
#     while i < len(nums):
#         if nums[i] in mapper:
#             return True
#         else:
#             mapper[nums[i]] = 1
#         i += 1
#     return False


def contains_duplicate(nums):
    mapper = {}
    for n in nums:
        if n in mapper:
            return True
        else:
            mapper[n] = 1
    return False


if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

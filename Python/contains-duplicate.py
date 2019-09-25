#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/contains-duplicate/


def contains_duplicate(nums):
    i = 0
    mapper = {}
    while i < len(nums):
        if nums[i] in mapper:
            return True
        else:
            mapper[nums[i]] = 1
        i += 1
    return False


if __name__ == '__main__':
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

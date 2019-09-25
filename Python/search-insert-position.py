#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/search-insert-position/


def search_insert(nums, target):
    i = 0
    while i < len(nums):
        if nums[i] >= target:
            return i
        i += 1
    return len(nums)


if __name__ == '__main__':
    print(search_insert([1, 3, 5, 6], 5))  # 2
    print(search_insert([1, 3, 5, 6], 2))  # 1
    print(search_insert([1, 3, 5, 6], 7))  # 4
    print(search_insert([1, 3, 5, 6], 0))  # 0
    print(search_insert([1], 0))  # 0
    print(search_insert([5], 5))  # 0

#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/single-number/
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/


def single_number(nums):
    nums.sort()
    i, n = 0, None
    while i < len(nums) - 2:
        if nums[i] != nums[i + 1]:
            n = nums[i]
            break
        i += 2
    return n if n is not None else nums[-1]


if __name__ == '__main__':
    print(single_number([2, 2, 1]))  # 1
    print(single_number([4, 1, 2, 1, 2]))  # 4

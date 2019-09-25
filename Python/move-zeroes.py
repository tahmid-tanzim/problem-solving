#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/move-zeroes/


def move_zeroes(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            j = i + 1
            while True:
                if j == len(nums) and nums[i] == 0:
                    j = i + 1
                elif j == len(nums) and nums[i] != 0:
                    break

                nums[j - 1] = nums[j]
                j += 1
            nums[j - 1] = 0
        i += 1
    print(nums)


if __name__ == '__main__':
    move_zeroes([0, 1, 0, 3, 12])
    # move_zeroes([0, 1, 0, 3, 12, 0, 9, 0])
    # move_zeroes([0, 0, 1])
    # move_zeroes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

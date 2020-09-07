#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/find-peak-element/


def find_peak_element(nums):
    i, mx = 0, {'i': 0, 'val': nums[0]}
    while i < len(nums):
        if nums[i] >= mx['val']:
            mx['i'] = i
            mx['val'] = nums[i]
        else:
            return mx['i']
        i += 1
    return mx['i']


if __name__ == '__main__':
    print(find_peak_element([1, 2, 3, 1]))
    print(find_peak_element([1, 2, 1, 3, 5, 6, 4]))
    print(find_peak_element([1]))

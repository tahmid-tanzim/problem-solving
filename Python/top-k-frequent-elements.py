#!/usr/local/bin/python3.6

import collections
"""
https://leetcode.com/problems/top-k-frequent-elements/
"""


def top_k_frequent(nums, K):
    x = {}
    for n in nums:
        if n in x.keys():
            x[n] += 1
        else:
            x[n] = 1
    return [k for k, v in sorted(x.items(), key=lambda item: item[1])][K * -1:]


# def top_k_frequent(nums, K):
#     count = collections.Counter(nums)
#     return count, K


if __name__ == '__main__':
    print(top_k_frequent(nums=[3, 3, 3, 1, 1, 1, 2, 2, 3], K=2))
    print(top_k_frequent(nums=[1], K=1))

#!/usr/bin/python3
# https://www.algoexpert.io/questions/Apartment%20Hunting
"""
  You're looking to move into a new apartment on specific street, and you're
  given a list of contiguous blocks on that street where each block contains an
  apartment that you could move into.

  You also have a list of requirements: a list of buildings that are important
  to you. For instance, you might value having a school and a gym near your
  apartment. The list of blocks that you have contains information at every
  block about all of the buildings that are present and absent at the block in
  question. For instance, for every block, you might know whether a school, a
  pool, an office, and a gym are present.

  In order to optimize your life, you want to pick an apartment block such that
  you minimize the farthest distance you'd have to walk from your apartment to
  reach any of your required buildings.

  Write a function that takes in a list of contiguous blocks on a specific
  street and a list of your required buildings and that returns the location
  (the index) of the block that's most optimal for you.

  If there are multiple most optimal blocks, your function can return the index
  of any one of them.

Sample Input
blocks = [
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": true,
    "school": false,
    "store": false,
  },
  {
    "gym": true,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": false,
  },
  {
    "gym": false,
    "school": true,
    "store": true,
  },
]
reqs = ["gym", "school", "store"]

Sample Output
3
// at index 3, the farthest you'd have to walk to reach a gym, a school,
// or a store is 1 block; at any other index, you'd have to walk farther
"""


# O(br) time | O(br) space
def apartmentHunting(blocks, reqs):
    totalBlocks = len(blocks)
    totalReqs = len(reqs)

    minDistanceTable = [
        [None for col in range(totalReqs)] for row in range(totalBlocks)
    ]

    for i in range(totalReqs):
        req = reqs[i]

        # Initialize First Block's Min Distance
        blockIdx = 0
        minDistanceTable[blockIdx][i] = 0 if blocks[blockIdx][req] else float('inf')

        # Forward Traverse
        for blockIdx in range(1, totalBlocks):
            if blocks[blockIdx][req]:
                minDistanceTable[blockIdx][i] = 0
            else:
                minDistanceTable[blockIdx][i] = minDistanceTable[blockIdx - 1][i] + 1 if minDistanceTable[blockIdx - 1][
                                                                                             i] is not None else float(
                    'inf')

        # Backward Traverse
        for blockIdx in range(totalBlocks - 2, -1, -1):
            if minDistanceTable[blockIdx][i] > minDistanceTable[blockIdx + 1][i]:
                minDistanceTable[blockIdx][i] = minDistanceTable[blockIdx + 1][i] + 1

    result = {
        "index": 0,
        "value": max(minDistanceTable[0])
    }

    for blockIdx in range(1, totalBlocks):
        minDistance = max(minDistanceTable[blockIdx])
        if result["value"] > minDistance:
            result = {
                "index": blockIdx,
                "value": minDistance
            }

    return result["index"]


if __name__ == '__main__':
    b = [
        {
            "gym": False,
            "school": True,
            "store": False,
        },
        {
            "gym": True,
            "school": False,
            "store": False,
        },
        {
            "gym": True,
            "school": True,
            "store": False,
        },
        {
            "gym": False,
            "school": True,
            "store": False,
        },
        {
            "gym": False,
            "school": True,
            "store": True,
        },
    ]
    r = ["gym", "school", "store"]
    print(f'{apartmentHunting(b, r)}')

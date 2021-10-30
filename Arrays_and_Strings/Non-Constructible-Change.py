#!/usr/bin/python3
# https://www.algoexpert.io/questions/Non-Constructible%20Change
"""
coins = [1, 2, 5]
the minimum amount of changes that you can't create is `4`.
If you're given no coins, the minimum amount of changes that you can't create is `1`.
"""


# Brute Force
def nonConstructibleChange1(coins):
    n = len(coins)
    coins.sort()
    amount = 1
    while True:
        total_value = amount
        for idx in range(n - 1, -1, -1):
            if total_value == 0:
                break
            if coins[idx] <= total_value:
                total_value -= coins[idx]
        if total_value > 0:
            return amount
        amount += 1


# Time Complexity - O(n log(n))
# Space Complexity - O(1)
def nonConstructibleChange2(coins):
    change = 0
    coins.sort()

    for coin in coins:
        if coin > change + 1:
            break
        change += coin

    return change + 1


if __name__ == '__main__':
    output1 = nonConstructibleChange1([5, 7, 1, 1, 2, 3, 22])
    print(f'{output1}')  # 20

    output2 = nonConstructibleChange2([5, 7, 1, 1, 2, 3, 22])
    print(f'{output2}')  # 20

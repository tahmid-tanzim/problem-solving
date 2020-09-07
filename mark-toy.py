def maximum_toys(prices, k):
    prices.sort()
    bucket = 0
    i = 0
    while i < len(prices) and bucket < k:
        bucket += prices[i]
        i += 1
    return i - 1


print(maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50))

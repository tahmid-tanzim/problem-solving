from collections import Counter

if __name__ == '__main__':
    amount = 0
    X = int(input())
    available_sizes = Counter([int(i) for i in input().split()])
    N = int(input())
    for i in range(N):
        size, price = map(int, input().split())
        if available_sizes[size] > 0:
            amount += price
            available_sizes[size] -= 1
    print(amount)


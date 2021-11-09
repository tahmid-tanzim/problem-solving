#!/usr/bin/python3


# Time Complexity O(n)
# Space Complexity O(n)
def recursiveFunction(n):
    if n == 0:
        return 0

    total = n + recursiveFunction(n - 1)
    print(f"n:{n} - total:{total}")
    return total


if __name__ == "__main__":
    output = recursiveFunction(6)
    print(output)

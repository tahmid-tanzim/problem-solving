#!/usr/bin/python3

"""
First, let’s mention that the trivial solution has the complexity of O(k). The problem can be solved by squaring and multiplying.

We know that p^k = p^x * p^y if x+y=k. We also know that p^k = (p^a)^b if a*b=k.

For an even value of k, choosing a = 2 and b = k/2, thus having p^k = (p^2)^(k/2), will reduce the number of required multiplications almost in half. For an odd value of k, choosing x = 1 and y=k-1 will result in y being even, and we can then simply repeat the same process as for the even case.
"""


# O(log k) where k is exponent
def pow(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return pow(base * base, exponent / 2)
    else:
        return base * pow(base * base, (exponent - 1) / 2)


if __name__ == "__main__":
    print(pow(2, 4))

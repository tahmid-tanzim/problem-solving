#!/usr/local/bin/python3.6

def set_annual():
    global annual
    annual = 120

def per_month():
    return annual / 2


if __name__ == '__main__':
    # (x, k) = tuple(map(int, input().split()))
    # P = input().replace("x", str(x))
    # print(eval(P) == k)

    set_annual()
    print(per_month())

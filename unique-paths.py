#!/usr/local/bin/python3


def unique_paths(m: int, n: int, memo: dict) -> int:
    # Base Case
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1

    key = f'{m}-{n}'
    if key in memo:
        return memo[key]

    move_down = unique_paths(m - 1, n, memo)
    move_right = unique_paths(m, n - 1, memo)
    memo[key] = move_down + move_right
    return memo[key]


if __name__ == "__main__":
    print(unique_paths(2, 3, {}))

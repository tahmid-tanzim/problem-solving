if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    x = 2
    y = 2
    z = 2
    n = 2

    # array = []
    # for xi in range(x + 1):
    #     for yi in range(y + 1):
    #         for zi in range(z + 1):
    #             if xi + yi + zi != n:
    #                 array.append([xi, yi, zi])
    # print(array)

    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])


def flipping_bits(n):
    flip_bits = ''
    b = "{0:0>32b}".format(n)
    for index in range(32):
        flip_bits += '0' if b[index] == '1' else '1'
    return int(flip_bits, 2)


if __name__ == '__main__':
    q = [2147483647, 1, 0]

    for i in range(3):
        result = flipping_bits(q[i])
        print(result)


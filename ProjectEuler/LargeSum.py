#!/usr/bin/puthon3
# https://projecteuler.net/problem=13

if __name__ == "__main__":
    total = 0
    with open('LargeSum-Input.txt', 'r', newline='') as file:
        i = 1
        for line in file.readlines():
            val = int(line)
            total += val
            print(i, line)
            i += 1
        file.close()

    print(f"\nTotal - {total}")

#!/usr/bin/python3

if __name__ == "__main__":
    last_item = 1
    prev_permutation = [2, 3]
    for i in range(len(prev_permutation) + 1):
        output_temp = prev_permutation.copy()
        output_temp.insert(i, last_item)
        print(f'{i} Prev Permutation - {prev_permutation} | Output - {output_temp}')

#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://www.hackerrank.com/challenges/dynamic-array/problem


def dynamic_array(n, queries):
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    output = []
    for Q, x, y in queries:
        index = (x ^ last_answer) % n
        if Q == 1:
            seq_list[index].append(y)
        if Q == 2:
            size = len(seq_list[index])
            last_answer = seq_list[index][y % size]
            output.append(last_answer)
    return output


if __name__ == '__main__':
    print(dynamic_array(2, [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
    ]))

#!/usr/local/bin/python3.6


def main():
    n = 2  # int(input())
    student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [25.0, 26.5, 28.0]}
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    query_name = 'Malika'  # input()

    sum = 0
    marks = student_marks[query_name]
    for i in marks:
        sum += i
    print("{:.2f}".format(sum/len(marks)))


if __name__ == '__main__': main()

#!/usr/local/bin/python3.6


def main():
    students = []
    names = []
    first = second = 100.0

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

        if score < first:
            second, first = first, score
        elif score < second and score != first:
            second = score

    for (name, score) in students:
        if second == score:
            names.append(name)

    for name in sorted(names):
        print(name)


if __name__ == '__main__':
    main()
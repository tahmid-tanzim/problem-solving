#!/usr/bin/python3


def main():
    n = int(input())
    output = []
    actions = []

    for _ in range(n):
        actions.append(input().split())

    for action in actions:
        if action[0] == 'insert':
            output.insert(int(action[1]), int(action[2]))
        elif action[0] == 'remove':
            output.remove(int(action[1]))
        elif action[0] == 'append':
            output.append(int(action[1]))
        elif action[0] == 'sort':
            output.sort()
        elif action[0] == 'pop':
            output.pop()
        elif action[0] == 'reverse':
            output.reverse()
        else:
            print(output)


if __name__ == '__main__':
    main()
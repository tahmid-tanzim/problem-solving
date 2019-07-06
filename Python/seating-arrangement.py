# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/

if __name__ == '__main__':
    T = int(input())
    a = []
    while T > 0:
        a.append(int(input()))
        T -= 1
    for i in reversed(a):
        print(i)

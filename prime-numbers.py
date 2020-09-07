N = int(input())
for num in range(N):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ')



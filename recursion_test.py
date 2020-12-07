#!/usr/local/bin/python3

def loop(n):
    if n == 1:
        return 1
    return n + loop(n - 1)  

if __name__ == "__main__":
   print(loop(10)) 
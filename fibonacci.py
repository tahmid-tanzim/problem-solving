class Fibonacci:
    def __init__(self) -> None:
        self.memoization_table = []

    def init_memo_table(self, n: int) -> None:
        self.memoization_table = [-1 for _ in range(n + 1)]

    # Method 1 (Use Recursion)
    def fib_num(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        if self.memoization_table[n] != -1:
            return self.memoization_table[n]

        self.memoization_table[n - 1] = self.fib_num(n - 1)
        self.memoization_table[n - 2] = self.fib_num(n - 2)
        return self.memoization_table[n - 1] + self.memoization_table[n - 2]

    # Method 2 (DP)
    # def get_fibonacci(self, n: int) -> int:
    #     # Initialization
    #     self.init_memo_table(n)
    #     self.memoization_table[0] = 0
    #     self.memoization_table[1] = 1


if __name__ == "__main__":
    inputs = [4, 5, 6]  # 4, 7, 12
    for i in inputs:
        f = Fibonacci()
        f.init_memo_table(i)
        print(f.fib_num(i), end='\n')

# Recursion

## 1. Find Time Complexity of Recursive Function
* Time Complexity - `O(branches ^ depth)`
* Space Complexity - `O(depth)`

By using Memoization / Caching precomputed results in a hashtable. We can improve the time complexity `O(depth)`

*Recurrence Relation*

```
       | 1           n=0           
T(n) = | 
       | T(n-1) + 2  n>0
```
## 2. Head Recursion (Linear Ascending)
* Time Complexity - `O(n)`
* Space Complexity - `O(n)`
```python
def printAscendingOrder(n: int):
    if n == 0:
        return 0
    printAscendingOrder(n - 1) 
    print(n)
```
## 3. Tail Recursion (Linear Descending)
* Time Complexity - `O(n)`
* Space Complexity - `O(n)`
```python
def printDescendingOrder(n: int):
    if n == 0:
        return 0
    print(n)
    printDescendingOrder(n - 1) 
```
## 4. Tree Recursion 
Tree Recursion is if a recursive function call itself more than once
### 4.1. Recursive Fibonacci Series without Memoization
* Time Complexity - `O(2 ^ n)`
* Space Complexity - `O(n)`
```python
def fib(n: int):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2) 
```
### 4.2. Recursive Fibonacci Series with Memoization
We can reduce time complexity from exponential to liner by using memoization technique.
* Time Complexity - `O(n)`
* Space Complexity - `O(n)`
```python
def fib(n: int, CACHE: dict = {}):
    if n <= 1:
        return n
    if n in CACHE:
        return CACHE[n]
    
    CACHE[n] = fib(n - 1, CACHE) + fib(n - 2, CACHE) 
    return CACHE[n]
```
### 4.3. Iterative Fibonacci Series 
* Time Complexity - `O(n)`
* Space Complexity - `O(1)`
```python
def fib(n: int):
    s = -1
    t0 = 0
    t1 = 1
    if n <= 1:
        return n
    for i in range(2, n + 1):
        s = t0 + t1
        t0 = t1
        t1 = s
    return s
```
## 5. Indirect Recursion 
If two or more function calling each other in a circular form.
```shell
(A) - (B)
  \   /
   (C)
```
Sample Code
```python
class Solution:
    def funcA(self, n: int):
        if n == 0:
            return
        print(n)
        self.funcB(n-1)
    
    def funcB(self, n: int):
        if n == 1:
            return 
        print(n)
        self.funcA(n//2)
```
## 6. Nested Recursion 
Sample Code
```python
def func(n: int):
    if n > 100:
        return n - 10 
    return func(func(n + 11))
```
## 7. Sum of first `n` natural numbers
n = 6
1 + 2 + 3 + 4 + 5 + 6 = 21

sum(n) = 1 + 2 + 3 + 4 + 5 + 6 + ... + (n - 2) + (n - 1) + n
sum(n) = sum(n-1) + n

*Recurrence Relation*
```
       | 0           n=0           
T(n) = | 
       | T(n-1) + n  n>0
```

### 7.1. Recursive Solution
* Time Complexity - `O(n)`
* Space Complexity - `O(n)` i.e. an activation record is pushed into the stack
```python
def sumOfNaturalNumbers(n):
    if n == 0:
        return 0
    return sumOfNaturalNumbers(n - 1) + n
```
### 7.2. Iterative Solution
* Time Complexity - `O(n)`
* Space Complexity - `O(1)`
```python
def sumOfNaturalNumbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```
### 7.3. Solution by using natural number formula
Formula - `T(n) = n * (n+1) / 2`
* Time Complexity - `O(1)`
* Space Complexity - `O(1)`
```python
def sumOfNaturalNumbers(n):
    return n * (n+1) // 2
```
## 8. Factorial
* Time Complexity - `O(n)`
* Space Complexity - `O(n)`
```python
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n
```
## 9. Power Calculation using Recursion
```markdown
2 ^ 5 = 2 * 2 * 2 * 2 * 2

m ^ n = m * m * m * ... for n times

pow(m, n) = m * m * m * ... * (n-1) times * m

pow(m, n) = pow(m, n-1) * m
```

*Recurrence Relation*
```
            | 1                 n=0           
pow(m, n) = | 
            | pow(m, n-1) * m   n>0
```
* Time Complexity - `O(m^n)`
* Space Complexity - `O(n)`
```python
def power(m, n):
    if n == 0:
        return 1
    return power(m, n-1) * m
```
Is there any better solution? Let's see ...
```markdown
2 ^ 8 = (2 ^ 2) ^ 4
2 ^ 8 = (2 * 2) ^ 4

2 ^ 9 = 2 * (2 ^ 2) ^ 4
```
i.e. if value of power is `even` then directly take half of the power.
And if the value of power is `odd` then one multiplication extra with half of the power
* Time Complexity - `O()`
* Space Complexity - `O()`
```python
def power2(m, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power2(m * m, n // 2)
    return m * power2(m * m, (n-1) // 2)
```
## 10. Combination Formula 
```markdown
nCr = n! / (r! * (n-r)!)

i.e. n = 5, 0 <= r <= n
```

```python
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n

# O(n) time, O(n) space 
def combination(n, r):
    t1 = factorial(n)
    t2 = factorial(r)
    t3 = factorial(n-r)
    return t1 / (t2 * t3)
```
### Pascal's Triangle
```markdown
              (1)
           /       \
         (1)       (1)
        /    \   /    \
      (1)     (2)     (1)
     /   \   /   \   /   \
   (1)    (3)      (3)     (1)
  /   \   /   \   /   \   /   \
(1)    (4)     (6)     (4)    (1)
```
Recursive Formula
```markdown
nCr = (n-1)C(r-1) + (n-1)Cr  
Base Case - return 1 when r == 0 and n == r  
4C2 = 3C1 + 3C2
```
Sample Code
```python
# O(n^r) time, O(n) space 
def nCr(n, r):
    if r == 0 and n == r :
        return 1
    return nCr(n - 1, r - 1) + nCr(n - 1, r)
```
## 11. Taylor Series 
```markdown
e^x = 1 + x/1 + x^2/2! + x^3/3! + x^4/4! + ... + n times

i.e. summation of x^n/n!
range of n is 0 <= n < &infin;
```


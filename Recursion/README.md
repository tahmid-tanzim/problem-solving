# Recursion

### Find Time Complexity of Recursive Function
* Time Complexity - `O(branches ^ depth)`
* Space Complexity - `O(depth)`

By using Memoization / Caching precomputed results in a hashtable. We can improve the time complexity `O(depth)`

*Recurrence Relation*

```
       | 1           n=0           
T(n) = | 
       | T(n-1) + 2  n>0
```
### Head Recursion (Linear Ascending)
* Time Complexity - `O(n)`
* Space Complexity - `O(n)`
```python
def printAscendingOrder(n: int):
    if n == 0:
        return 0
    printAscendingOrder(n - 1) 
    print(n)
```
### Tail Recursion (Linear Descending)
* Time Complexity - `O(n)`
* Space Complexity - `O(n)`
```python
def printDescendingOrder(n: int):
    if n == 0:
        return 0
    print(n)
    printDescendingOrder(n - 1) 
```
### Tree Recursion 
Tree Recursion is if a recursive function call itself more than once
#### Without Memoization
* Time Complexity - `O(2 ^ n)`
* Space Complexity - `O(n)`
```python
def fib(n: int):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2) 
```
#### Memoization
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
### Indirect Recursion 
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
### Nested Recursion 
Sample Code
```python
def func(n: int):
    if n > 100:
        return n - 10 
    return func(func(n + 11))
```
### Sum of first `n` natural numbers
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

#### Recursive Solution
* Time Complexity - `O(n)`
* Space Complexity - `O(n)` i.e. an activation record is pushed into the stack
```python
def sumOfNaturalNumbers(n):
    if n == 0:
        return 0
    return sumOfNaturalNumbers(n - 1) + n
```
#### Iterative Solution
* Time Complexity - `O(n)`
* Space Complexity - `O(1)`
```python
def sumOfNaturalNumbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```
#### Solution by using natural number formula
Formula - `T(n) = n * (n+1) / 2`
* Time Complexity - `O(1)`
* Space Complexity - `O(1)`
```python
def sumOfNaturalNumbers(n):
    return n * (n+1) // 2
```
### Factorial
* Time Complexity - `O(n)`
* Space Complexity - `O(n)`
```python
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n
```
### Power Calculation using Recursion
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
    else:
        return m * power2(m * m, (n-1) / 2)
```
# Problem Solving
Coding Interview Preparation
### 1. Asymptotic Notations

**Big O Complexity Chart**

![time complexity graph](https://adrianmejia.com/images/time-complexity-examples.png?raw=true)

```markdown
1 < log(n) < n < n*log(n) < n^2 < n^3 < ... < 2^n < 3^n < ... < n^n

<Polynomial>
    1 < log(n) < n < n*log(n) < n^2 < n^3 ...
</Polynomial>  

<Exponential>
    2^n < 3^n < ... < n^n
</Exponential>
```
1. Lower Bound - `Ω` Omega
2. Upper Bound - `O` Big-O
3. Tight Bound - `Θ` Theta

[Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
### 2. [Heap - Heap Sort - Heapify - Priority Queues](Heap/README.md)
### 3. [Recursion](Recursion/README.md)
### 4. [Dynamic Programming](Dynamic_Programming/README.md)
### 5. [Array and Strings](Arrays_and_Strings/README.md)
### 6. [Trees and Graphs](Trees_and_Graphs/README.md)
### 7. [0/1 Knapsack](Dynamic_Programming/01-knapsack-problem.py)
    Unbounded knapsack 
    Fractional Greedy
    Memoization
    Top Down
### 8. [Knapsack variation Problem](Dynamic_Programming/6-type-knapsack-problem.py)
    8.1. Subset Sum Problem ~> [Link](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
    8.2. Equal Subset Sum Partition ~> [Link](https://www.youtube.com/watch?v=UmMh7xp07kY)
    8.3. Count of Subset Sum
    8.4. Minimum Subset Sum Difference
    8.5. Number of Subset by a given Difference
    8.6. Target Sum DP
### 9. [Backtracking Problems](https://leetcode.com/discuss/interview-question/1098081/Famous-Backtracking-Problems)
### 10. Searching & Sorting
    10.1. How do I identify cyclic sort pattern?
          - They will be problems involving a sorted array with numbers in a given range
          - If the problem asks you to find the missing/duplicate/smallest number in an sorted/rotated array
### 11. System Design
    11.1. [System Design Primer](https://github.com/tahmid-tanzim/system-design-primer)
    11.2. [LeetCode posts on System Design](https://leetcode.com/discuss/interview-question/1140451/helpful-list-of-leetcode-posts-on-system-design-at-facebook-google-amazon-uber-microsoft)
### 12. [Python - Pipenv](https://docs.python-guide.org/dev/virtualenvs/)
```shell
$ python3 -m pip install --upgrade pip
$ python3 -m pip install virtualenv
$ virtualenv --version
$ virtualenv project_workspace
$ cd project_workspace
$ source bin/activate
$ pip install requests
$ pip freeze > requirements.txt
$ deactivate
$ pip install -r requirements.txt
```
### 13. [Python Virtual Environments](https://docs.python.org/3/library/venv.html)
```shell
$ python3 -m venv env
$ source env/bin/activate
$ pip install --upgrade pip
$ pip install django
$ pip install djangorestframework
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
$ deactivate
```
### 14. SQL Group by time
Hourly Group By
```sql
SELECT
    restaurant,
    DATE_TRUNC('hour', payment_time) AT TIME ZONE 'America/New_York' AS payment_datetime,
    COUNT(id) AS total
FROM
    payments
WHERE payment_time AT TIME ZONE 'America/New_York' BETWEEN '2023-04-03 00:00:00' AND '2023-04-03 23:59:59'
AND restaurant IN ('tim_hortons','mcdonalds','kfc')
GROUP BY restaurant, payment_datetime;
```

15 Minutes Group By
```sql
SELECT
    restaurant,
    TO_TIMESTAMP(FLOOR((EXTRACT('epoch' FROM payment_time) / 900 )) * 900) AT TIME ZONE 'America/New_York' AS payment_datetime,
    COUNT(id) AS total
FROM
    payments
WHERE payment_time AT TIME ZONE 'America/New_York' BETWEEN '2023-04-03 00:00:00' AND '2023-04-03 23:59:59'
AND restaurant IN ('tim_hortons','mcdonalds','kfc')
GROUP BY restaurant, payment_datetime;```

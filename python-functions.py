# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.

n = (5)

def sum_to(n):
  return sum(range(n+1))

print(sum_to(n))

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
  return max(list)

print(largest([10, 4, 2, 231, 91, 54]))


# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.

n = (5)

def sum_to(n):
  return sum(range(n+1))

print(sum_to(n))

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
  return max(list)

print(largest([10, 4, 2, 231, 91, 54]))

# 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurances(string, substring):
  return string.count(substring)

print(occurances('fleep floop', 'fe'))

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  num = 1
  for arg in args:
    num *= arg
  return num

print(product(4, 0.5, 5))
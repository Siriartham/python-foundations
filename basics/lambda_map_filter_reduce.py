"""
Lambda functions are anonymous functions used for
short, simple operations.
This file demonstrates lambda usage with map,
filter, and reduce.
"""

from functools import reduce

# Normal function
def add(a, b):
    return a + b

print("Using normal function:", add(5, 2))

# Lambda function
add_lambda = lambda x, y: x + y
print("Using lambda function:", add_lambda(8, 6))


# FILTER: select even numbers
numbers = [1, 3, 5, 12, 34, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# MAP: double each number
nums = [93, 87, 556, 18, 189, 34, 55, 23, 12]
doubled_nums = list(map(lambda x: x * 2, nums))
print("Doubled values:", doubled_nums)


# REDUCE: sum of all numbers
values = [33, 23, 55, 23, 44, 12]
total_sum = reduce(lambda x, y: x + y, values)
print("Sum using reduce:", total_sum)

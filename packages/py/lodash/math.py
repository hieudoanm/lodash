import math

def add(a, b):
  return a + b

def ceil(number):
  return math.ceil(number)

def divide(a, b):
  return a / b

def floor(number):
  return math.floor(number)

def max(numbers):
  if len(numbers) == 0:
    return
  max = float('-inf')
  for number in numbers:
    if number > max:
      max = number
  return max

def maxBy(objects, iteratee):
  if len(objects) == 0:
    return
  numbers = []
  for obj in objects:
    number = obj[iteratee]
    numbers.append(number)
  return max(numbers)

def mean(numbers):
  length = len(numbers)
  if length == 0:
    return 0
  _sum = sum(numbers)
  return _sum / length

def meanBy(objects, iteratee):
  if len(objects) == 0:
    return
  numbers = []
  for obj in objects:
    number = obj[iteratee]
    numbers.append(number)
  return mean(numbers)

def min(numbers):
  if len(numbers) == 0:
    return
  min = float('inf')
  for number in numbers:
    if number < min:
      min = number
  return min

def minBy(objects, iteratee):
  if len(objects) == 0:
    return
  numbers = []
  for obj in objects:
    number = obj[iteratee]
    numbers.append(number)
  return min(numbers)

def multiply(a, b):
  return a * b

def roundNumber(number, precision = 0):
  return round(number, precision)

def subtract(a, b):
  return a - b

# Recursion
def sum(numbers):
  if len(numbers) == 0:
    return 0
  first = numbers.pop(0);
  return first + sum(numbers);

def sumBy(objects, iteratee):
  if len(objects) == 0:
    return
  numbers = []
  for obj in objects:
    number = obj[iteratee]
    numbers.append(number)
  return sum(numbers)

import random as rand

def clamp(number, lower, upper):
  if lower > upper:
    return
  if number < lower:
    return lower
  elif number > upper:
    return upper
  else:
    return number

def inRange(number, x, y = None):
  start = 0
  stop = x
  if y is not None:
    start = x
    stop = y
  return start < number and number < stop

def random(x, y = None, step = 1):
  start = 0
  end = x
  if y is not None:
    start = x
    end = y
  return rand.randrange(start, end, step)

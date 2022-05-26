import uuid

def constant(value):
  return value

def defaultTo(value, defaultValue):
  if value == None:
    return defaultValue
  return value

def identity(*args):
  value = args[0]
  return value

def noop():
  return None

def rangeArray(_start, _end = None, step = 1):
  start = 0
  end = _start
  if _end != None:
    start = _start
    end = _end
  array = [*range(start, end, step)]
  return array

def rangeRight(start, end = None, step = 1):
  array = rangeArray(start, end, step)
  array.reverse()
  return array

def stubArray():
  return []

def stubFalse():
  return False

def stubObject():
  return {}

def stubString():
  return ''

def stubTrue():
  return True

def times(n, callback = None):
  array = [*range(0, n, 1)]
  if callback == None:
    return array
  for index, _ in enumerate(array):
    array[index] = callback
  return array
  
def toPath(value):
  value = value.replace("[", ".")
  value = value.replace("]", ".")
  return value.split(".")

def uniqueId(prefix = ''):
  return prefix + str(uuid.uuid4())
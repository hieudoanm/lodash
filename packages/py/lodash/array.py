import copy

def chunk(array, size = 1):
  newArray = []
  for i in range(0, len(array), size):
    newArray.append(array[i:i + size])
  return newArray

def compact(array):
  newArray = []
  for item in array:
    if item:
      newArray.append(item)
  return newArray

def concat(array, *args):
  newArray = array
  for arg in args:
    if isinstance(arg, list):
      for item in arg:
        newArray.append(item)
    else:
      newArray.append(arg)
  return newArray

def difference(array, values):
  if len(array) == 0:
    return []
  _difference = []
  for i in array:
    if i not in values:
      _difference.append(i)
  return _difference

def differenceBy(array, values, callback):
  newValues = []
  for value in values:
    newValues.append(callback(value))
  newArray = []
  for item in array:
    if callback(item) not in newValues:
      newArray.append(item)
  return newArray

def drop(array, n = 1):
  return array[n:len(array)]

def dropRight(array, n = 1):
  if n >= len(array):
    return []
  return array[0:len(array) - n]

def dropRightWhile(array, callback):
  tempArray = copy.deepcopy(array)
  tempArray.reverse()
  for item in tempArray:
    flag = callback(item)
    if flag:
      array.remove(item)

def dropWhile(array, callback):
  tempArray = copy.deepcopy(array)
  for item in tempArray:
    flag = callback(item)
    if flag:
      array.remove(item)

def fill(array, value, start = 0, end = None):
  if end is None:
    end = len(array)
  for index, item in enumerate(array):
    if index < start or index > end - 1:
      array[index] = item
    else:
      array[index] = value
  return array

# Linear Search
def findIndex(array, callback, fromIndex = 0):
  newArray = array[fromIndex:]
  index = -1
  for idx, item in enumerate(newArray):
    flag = callback(item)
    if flag:
      index = idx
      break
  return index

def findLastIndex(array, callback, fromIndex = None):
  newArray = array[0:fromIndex]
  index = -1
  for idx, item in enumerate(newArray):
    flag = callback(item)
    if flag:
      index = idx
  return index

def flatten(array):
  newArray = []
  for item in array:
    if isinstance(item, list):
      newArray = concat(newArray, item)
    else:
      newArray.append(item)
  return newArray

def flattenDeep(array):
  if array == []:
    return array
  if isinstance(array[0], list):
    return flattenDeep(array[0]) + flattenDeep(array[1:])
  return array[:1] + flattenDeep(array[1:])

def flattenDepth(array, depth = 1):
  newArray = array
  for _ in range(0, depth):
    newArray = flatten(newArray)
  return newArray

def fromPairs(pairs):
  object = {}
  for pair in pairs:
    key, value = pair
    object[key] = value
  return object

def head(array):
  if len(array) == 0:
    return
  return array[0]

def indexOf(array, value, fromIndex = 0):
  if fromIndex >= len(array):
    return -1
  return array[fromIndex:len(array)].index(value) + fromIndex

def initial(array):
  return array[0:len(array) - 1]

def intersection(*args):
  arrays = list(args)
  total = len(arrays)
  flattenArray = flattenDeep(arrays)
  itemCount = {}
  for item in flattenArray:
    if item in itemCount:
      itemCount[item] += 1
    else:
      itemCount[item] = 1
  array = []
  for key in itemCount.keys():
    if itemCount[key] == total:
      array.append(key)
  return array

def join(array, separator):
  return separator.join(array)

def last(array):
  if len(array) == 0:
    return
  return array[len(array) - 1]

def lastIndexOf(array, value, fromIndex = None):
  newArray = array[0:fromIndex]
  index = -1
  for idx, item in enumerate(newArray):
    if item == value:
      index = idx
  return index

def nth(array, n):
  return array[n]

def pull(array, *args):
  values = list(args)
  tempArray = copy.deepcopy(array)
  for item in tempArray:
    if item in values:
      array.remove(item)
    
def pullAll(array, values):
  tempArray = copy.deepcopy(array)
  for item in tempArray:
    if item in values:
      array.remove(item)
    
def pullAt(array, indexes):
  tempArray = copy.deepcopy(array)
  removedArray = []
  for index, item in enumerate(tempArray):
    if index in indexes:
      array.remove(item)
      removedArray.append(item)
  return removedArray

def remove(array, callback):
  newArray = []
  tempArray = copy.deepcopy(array)
  for item in tempArray:
    flag = callback(item)
    if flag:
      array.remove(item)
      newArray.append(item)
  return newArray

# Recursion
def reverse(array):
  if len(array) == 0:
    return []
  sub = array[1:]
  reverseSub = reverse(sub)
  reverseSub.append(array[0])
  return reverseSub

def slice(array, start = 0, end = None):
  return array[start:end]

def sortedIndex(array, value):
  index = -1
  for idx, _ in enumerate(array):
    if idx < len(array) - 1:
      first = array[idx]
      second = array[idx + 1]
      if first <= value and value <= second:
        index = idx + 1
        break
    else:
      idx = index + 1
  return index

def sortedLastIndex(array, value):
  index = -1
  for idx, _ in enumerate(array):
    if idx < len(array) - 1:
      first = array[idx]
      second = array[idx + 1]
      if first <= value and value <= second:
        index = idx + 1
    else:
      idx = index + 1
  return index

def sortedUniq(array):
  newArray = []
  for item in array:
    if item not in newArray:
      newArray.append(item)
  return newArray

def tail(array):
  return array[1:len(array)]

def take(array, n = 1):
  return array[0:n]

def takeRight(array, n = 1):
  length = len(array)
  start = length - n if length - n >= 0 else 0
  return array[start:length]

def takeRightWhile(array, callback):
  tempArray = copy.deepcopy(array)
  tempArray.reverse()
  for item in tempArray:
    flag = callback(item)
    if not flag:
      array.remove(item)

def takeWhile(array, callback):
  tempArray = copy.deepcopy(array)
  for item in tempArray:
    flag = callback(item)
    if not flag:
      array.remove(item)

def union(*args):
  arrays = list(args)
  newArray = []
  for array in arrays:
    for item in array:
      if item not in newArray:
        newArray.append(item)
  return newArray

def uniq(array):
  return list(set(array))
  
def unzip(arrays):
  totalItemsPerArray = len(arrays)
  totalArrays = 0
  for array in arrays:
    if totalArrays < len(array):
      totalArrays = len(array)
  newArray = []
  for idx1 in range(0, totalArrays):
    newArray.append([])
    for idx2 in range(0, totalItemsPerArray):
      value = arrays[idx2][idx1]
      newArray[idx1].append(value)
  return newArray

def unzipWith(arrays, callback):
  unzipped = unzip(arrays)
  newArray = []
  for array in unzipped:
    value = callback(*array)
    newArray.append(value)
  return newArray

def without(array, *args):
  values = list(args)
  newArray = []
  for item in array:
    if item not in values:
      newArray.append(item)
  return newArray

def xor(*args):
  arrays = list(args)
  flattenArray = flattenDeep(arrays)
  itemCount = {}
  for item in flattenArray:
    if item in itemCount:
      itemCount[item] += 1
    else:
      itemCount[item] = 1
  array = []
  for key in itemCount.keys():
    if itemCount[key] == 1:
      array.append(key)
  return array

def zip(*args):
  arrays = list(args)
  maximum = 0
  for array in arrays:
    if maximum < len(array):
      maximum = len(array)
  newArrays = []
  def getItem(array, i):
    try:
      return array[i]
    except:
      return None
  for i in range(0, maximum):
    newArray = []
    for array in arrays:
      item = getItem(array, i)
      newArray.append(item)
    newArrays.append(newArray)
  return newArrays

def zipObject(props, values):
  obj = {}
  for index, prop in enumerate(props):
    value = None
    if index < len(values):
      value = values[index]
    obj[prop] = value
  return obj

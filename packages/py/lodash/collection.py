import copy
import random as rand

from .array import flatten, flattenDeep, flattenDepth

def countBy(array, callback):
  obj = {}
  for item in array:
    key = callback(item)
    if key not in obj:
      obj[key] = 1
    else:
      obj[key] += 1
  return obj

def every(array, callback):
  flag = True
  for item in array:
    if not callback(item):
      flag = False
      break
  return flag

def filter(array, callback):
  newArray = []
  for item in array:
    if callback(item):
      newArray.append(item)
  return newArray

def find(array, predicate, fromIndex = 0):
  filtered = filter(array[fromIndex:len(array)], predicate)
  if len(filtered) == 0:
    return None
  return filtered[0]

def findLast(array, predicate, fromIndex = 0):
  filtered = filter(array[fromIndex:len(array)], predicate)
  if len(filtered) == 0:
    return None
  return filtered[len(filtered) - 1]

def flatMap(collection, callback):
  newArray = []
  for item in collection:
    newItem = callback(item)
    newArray.append(newItem)
  return flatten(newArray)

def flatMapDeep(collection, callback):
  newArray = []
  for item in collection:
    newItem = callback(item)
    newArray.append(newItem)
  return flattenDeep(newArray)

def flatMapDepth(collection, callback, depth = 1):
  newArray = []
  for item in collection:
    newItem = callback(item)
    newArray.append(newItem)
  return flattenDepth(newArray, depth)

def forEach(array, callback):
  for item in array:
    callback(item)
  
def forEachRight(array, callback):
  array.reverse()
  forEach(array, callback)

def groupBy(array, callback):
  obj = {}
  for item in array:
    key = str(callback(item))
    if key in obj:
      obj[key].append(item)
    else:
      obj[key] = [item]
  return obj

def includes(array, value, fromIndex = 0):
  return value in array[fromIndex:len(array)]

def invokeMap(collection, callback, *args):
  newArray = []
  for item in collection:
    newItem = callback(item, *args)
    newArray.append(newItem)
  return newArray

def keyBy(array, callback):
  obj = {}
  for item in array:
    key = callback(item)
    obj[key] = item
  return obj

def map(array, callback):
  newArray = []
  for item in array:
    newItem = callback(item)
    newArray.append(newItem)
  return newArray

def partition(array, callback):
  truthy = filter(array, callback)
  falsey = reject(array, callback)
  return [truthy, falsey]

def reduce(collection, callback, accumulator):
  if isinstance(collection, list):
    for item in collection:
      accumulator = callback(accumulator, item)
    return accumulator
  if isinstance(collection, dict):
    for key in collection.keys():
      value = collection[key]
      accumulator = callback(accumulator, value, key)
  return accumulator

def reduceRight(collection, callback, accumulator):
  if isinstance(collection, list):
    collection.reverse()
    for item in collection:
      accumulator = callback(accumulator, item)
    return accumulator
  if isinstance(collection, dict):
    keys = collection.keys()
    keys.reverse()
    for key in keys:
      value = collection[key]
      accumulator = callback(accumulator, value, key)
  return accumulator

def reject(array, callback):
  return filter(array, lambda i: not callback(i))

def sample(array):
  index = rand.randrange(0, len(array))
  return array[index]

def sampleSize(array, n):
  if n >= len(array):
    return array
  newArray = copy.deepcopy(array)
  rand.shuffle(newArray)
  return newArray[0:n]

def shuffle(array):
  rand.shuffle(array)

def size(collection):
  if isinstance(collection, str) or isinstance(collection, list):
    return len(collection)
  elif isinstance(collection, dict):
    return len(collection.keys())
  return 0
  
def some(array, callback):
  flag = False
  for item in array:
    if callback(item):
      flag = True
      break
  return flag

def sortBy(array, key):
  return sorted(array, key=lambda d: d[key]) 

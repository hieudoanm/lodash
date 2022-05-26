from .lang import isFunction

def assign(obj, *args):
  for arg in args:
    for key in arg:
      value = arg[key]
      obj[key] = value
  return obj

def at(object, paths):
  array = []
  for path in paths:
    value = get(object, path)
    array.append(value)
  return array
  
def defaults(*args):
  objects = list(args)
  objects.reverse()
  obj = {}
  for item in objects:
    for key in item.keys():
      value = item[key]
      obj[key] = value
  return obj

def findKey(object, callback):
  _keys = keys(object)
  newKeys = []
  for key in _keys:
    value = object[key]
    if callback(value):
      newKeys.append(key)
  if len(newKeys) > 0:
    return newKeys[0]
  return None

def findLastKey(object, callback):
  _keys = keys(object)
  _keys.reverse()
  newKeys = []
  for key in _keys:
    value = object[key]
    if callback(value):
      newKeys.append(key)
  if len(newKeys) > 0:
    return newKeys[0]
  return None

def forIn(object, callback):
  _keys = keys(object)
  for key in _keys:
    value = object[key]
    callback(value, key)

def forInRight(object, callback):
  _keys = keys(object)
  _keys.reverse()
  for key in _keys:
    value = object[key]
    callback(value, key)

def forOwn(object, callback):
  forIn(object, callback)

def forOwnRight(object, callback):
  forInRight(object, callback)
  
def functions(object):
  _keys = keys(object)
  newArray = []
  for key in _keys:
    value = object[key]
    newArray.append(value)
  return newArray

def functionsIn(object):
  return functions(object)

def get(obj, path, defaultValue = None):
  hasPath = has(obj, path)
  if not hasPath:
    return defaultValue
  keys = path.split('.')
  value = obj
  for key in keys:
    value = value.get(key)
  return value

def has(obj, path):
  keys = path.split('.')
  flag = True
  nested = obj
  for key in keys:
    if not isinstance(nested, dict):
      flag = False
      break
    if key in nested:
      nested = nested[key]
    else:
      flag = False
      break
  return flag

def invert(obj):
  newObj = {}
  _keys = keys(obj)
  for key in _keys:
    value = obj[key]
    newKey = str(value)
    newObj[newKey] = key
  return newObj

def invertBy(obj, callback = None):
  newObj = {}
  _keys = keys(obj)
  for key in _keys:
    value = obj[key]
    newKey = str(value)
    if isFunction(callback):
      newKey = callback(value)
    if newKey in newObj:
      newObj[newKey].append(key)
    else:
      newObj[newKey] = [key]
  return newObj

def keys(obj):
  return list(obj.keys())

def keysIn(obj):
  return list(obj.keys())

def mapKeys(obj, callback):
  oldKeys = keys(obj)
  newObj = {}
  for key in oldKeys:
    value = obj[key]
    newKey = callback(value, key)
    newObj[newKey] = value
  return newObj

def mapValues(obj, callback):
  _keys = keys(obj)
  for key in _keys:
    value = obj[key]
    newValue = callback(value)
    obj[key] = newValue
  return obj

def omit(obj, paths):
  newObject = {}
  _keys = keys(obj)
  for key in _keys:
    if key not in paths:
      value = obj[key]
      newObject[key] = value
  return newObject

def omitBy(obj, callback):
  newObject = {}
  _keys = keys(obj)
  for key in _keys:
    value = obj[key]
    flag = callback(value)
    if not flag:
      newObject[key] = value
  return newObject

def pick(obj, paths):
  newObj = {}
  for path in paths:
    value = get(obj, path)
    setObject(newObj, path, value)
  return newObj

def pickBy(obj, callback):
  newObj = {}
  _keys = keys(obj)
  for key in _keys:
    value = get(obj, key)
    flag = callback(value)
    if flag:
      setObject(newObj, key, value)
  return newObj

def result(obj, path, defaultValue = None):
  callback = get(obj, path, defaultValue)
  if not callable(callback):
    return callback
  value = callback()
  if value == None:
    return defaultValue
  return value

def setObject(obj, path, value):
  keys = path.split(".")
  if len(keys) == 1:
    obj[keys[0]] = value
  else:
    key = keys[0]
    objectValue = setObject({}, ".".join(keys[1:len(keys)]), value)
    obj[key] = objectValue
  return obj

def toPairs(obj):
  array = []
  for key in obj:
    value = obj[key]
    array.append([key, value])
  return array
  
def toPairsIn(obj):
  return toPairs(obj)

def update(obj, path, updater):
  oldValue = get(obj, path)
  if oldValue == None:
    return obj
  newValue = updater(oldValue)
  newObj = setObject(obj, path, newValue)
  return newObj

def values(obj):
  return list(obj.values())

def valuesIn(obj):
  return values(obj)

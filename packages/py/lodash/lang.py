import copy
import math
import sys

def castArray(value):
  return [value]

def conformsTo(object, source):
  keys = list(source.keys())
  key = keys[0]
  value = object[key]
  return source[key](value)

def clone(value):
  return copy.copy(value)

def cloneDeep(value):
  return copy.deepcopy(value)

def cloneDeepWith(value, customizer):
  deep = cloneDeep(value)
  return customizer(deep)

def cloneWith(value, customizer):
  shallow = clone(value)
  return customizer(shallow)

def eq(value, other):
  return value == other

def gt(value, other):
  return value > other

def gte(value, other):
  return value >= other

def isArray(value):
  return isinstance(value, list)

def isArrayLike(value):
  return isinstance(value, list) or isinstance(value, str)

def isArrayLikeObject(value):
  return isinstance(value, list)

def isBoolean(value):
  return isinstance(value, bool)

def isEmpty(value):
  if isinstance(value, list) and len(value) > 0:
    return False
  if isinstance(value, dict) and len(list(value.keys())) > 0:
    return False
  return True

def isEqual(value, other):
  return value == other

def isEqualWith(value, other, customizer):
  return customizer(value) and customizer(other)

def isFinite(value):
  if not isNumber(value):
    return False
  return math.isfinite(value)

def isFunction(value):
  return str(type(value)) == "<class 'function'>"

def isInteger(value):
  return isinstance(value, int)

def isLength(value):
  return isInteger(value)

def isMatch(obj, source):
  _keys = list(source.keys())
  flag = True
  for key in _keys:
    if obj[key] != source[key]:
      flag = False
      break
  return flag

def isMatchWith(obj, source, customizer):
  _keys = list(source.keys())
  flag = True
  for key in _keys:
    if customizer(obj[key]) != customizer(source[key]):
      flag = False
      break
  return flag

def isNil(value):
  return value == None

def isNull(value):
  return value == None

def isNumber(value):
  return isinstance(value, float) or isinstance(value, int)  

def isObject(value):
  return isinstance(value, dict)

def isObjectLike(value):
  return isinstance(value, dict) or isinstance(value, list)

def isSafeInteger(value):
  if not isinstance(value, int):
    return False
  upper = sys.maxsize
  lower = - upper - 1
  return lower < value and value < upper
  
def isSet(value):
  return isinstance(value, set)

def isString(value):
  return isinstance(value, str)

def isUndefined(value):
  return value == None

def lt(value, other):
  return value < other

def lte(value, other):
  return value <= other

def toArray(value):
  if isinstance(value, dict):
    return list(value.values())
  if isinstance(value, str):
    return [c for c in value]
  if isinstance(value, list):
    return value
  return []

def toInteger(value):
  if isinstance(value, str):
    return int(float(value))
  return int(value)

def toLength(value):
  return toInteger(value)

def toNumber(value):
  return float(value)

def toSafeInteger(value):
  upper = sys.maxsize
  lower = - upper - 1
  if value < lower:
    return lower
  elif value > upper:
    return upper
  if not isinstance(value, int):
    value = int(value)
  return value

def toString(value):
  if value is None:
    return ''
  return str(value)

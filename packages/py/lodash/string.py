import math

def camelCase(string):
  array = split(string, ' ')
  first = array[0].lower()
  newArray = []
  for char in array[1:len(array)]:
    newChar = capitalize(char)
    newArray.append(newChar)
  newArray.insert(0, first)
  return "".join(newArray)

def capitalize(string):
  first = string[0].capitalize()
  rest = string[1:len(string)].lower()
  return first + rest

def endsWith(string, target, position = 1):
  return string[len(string) - position] == target

def kebabCase(string):
  array1 = split(string, ' ')
  array2 = []
  for item in array1:
    newItem = item.lower()
    array2.append(newItem)
  return "-".join(array2)

def lowerCase(string):
  newArray = []
  for char in string:
    newItem = char if char.isalpha() else ' '
    newArray.append(newItem)
  result = "".join(newArray).lower().strip()
  return " ".join(result.split())

def lowerFirst(string):
  first = string[0].lower()
  return first + string[1:len(string)]

def pad(string, length = 0, chars = ' '):
  padding = length - len(string)
  if padding <= 0:
    return string
  paddingStart = math.floor(padding / 2)
  paddingEnd = padding - paddingStart
  start = (chars * paddingStart)[0:paddingStart]
  end = (chars * paddingEnd)[0:paddingEnd]
  return start + string + end

def padEnd(string, length = 0, chars = ' '):
  padding = length - len(string)
  end = (chars * padding)[0:padding]
  return string + end

def padStart(string, length = 0, chars = ' '):
  padding = length - len(string)
  start = (chars * padding)[0:padding]
  return start + string

def parseInt(string):
  return int(string)

def repeat(string, n):
  return string * n

def replace(string, pattern, replacement):
  return string.replace(pattern, replacement)

def snakeCase(string):
  array1 = split(string, ' ')
  array2 = []
  for item in array1:
    newItem = item.lower()
    array2.append(newItem)
  return "_".join(array2)

def split(value, separator = '', limit = None):
  string = str(value)
  if separator == '':
    return [c for c in string]
  array = string.split(separator)
  return array[0:limit]

def startCase(string):
  array1 = []
  for char in string:
    newItem = char if char.isalpha() else ' '
    array1.append(newItem)
  result = "".join(array1).lower().strip()
  array2 = []
  for word in result.split():
    array2.append(capitalize(word))
  return " ".join(array2)

def startsWith(string, target, position = 0):
  return string[position] == target

def toLower(string):
  return string.lower()

def toUpper(string):
  return string.upper()

def trim(string):
  return string.strip()

def trimEnd(string):
  return string.rstrip()

def trimStart(string):
  return string.lstrip()

def truncate(string, length = 30, omission = "..."):
  omissionLen = len(omission)
  short = length - omissionLen
  return string[0:short] + " " + omission

def upperCase(string):
  newArray = []
  for char in string:
    newItem = char if char.isalpha() else ' '
    newArray.append(newItem)
  result = "".join(newArray).upper().strip()
  return " ".join(result.split())

def upperFirst(string):
  return string.capitalize()

def words(string):
  newArray = []
  for char in string:
    newItem = char if char.isalpha() else ' '
    newArray.append(newItem)
  result = "".join(newArray).strip()
  return result.split()
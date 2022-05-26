import time

def debounce(func, wait = 0):
  time.sleep(wait)
  func()

def delay(func, wait = 0, *args):
  time.sleep(wait)
  func(*args)
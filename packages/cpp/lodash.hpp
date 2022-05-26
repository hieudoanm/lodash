#include "iostream"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

// Array
template <typename T>
T head(T array[]) {
  return array[0];
}
template <typename T>
T last(T array[], int size) {
  return array[size - 1];
}
template <typename T>
T nth(T array[], int n, int size) {
  if (n < 0) {
    return array[size + n];
  }
  return array[n];
}
// Lang
template <typename T>
bool gt(T value, T other) {
  return value > other;
}
template <typename T>
bool gte(T value, T other) {
  return value >= other;
}
template <typename T>
bool lt(T value, T other) {
  return value < other;
}
template <typename T>
bool lte(T value, T other) {
  return value <= other;
}
// Math
template <typename T>
T add(T a, T b) {
  return a + b;
}
template <typename T>
T divide(T a, T b) {
  return a / b;
}
template <typename T>
T multiply(T a, T b) {
  return a * b;
}
template <typename T>
T subtract(T a, T b) {
  return a - b;
}
// Number
template <typename T>
T clamp(T number, T lower, T upper) {
  if (lower > upper) {
    T temp = lower;
    lower = upper;
    upper = temp;
  }
  if (number < lower) {
    return lower;
  }
  if (number > upper) {
    return upper;
  }
  return number;
}
template <typename T>
T inRange(T number, T start, T end) {
  if (start > end) {
    T temp = end;
    end = start;
    start = temp;
  }
  return start < number && number < end;
}
template <typename T>
T random(T lower, T upper) {
  if (lower > upper) {
    T temp = lower;
    lower = upper;
    upper = temp;
  }
  srand((unsigned) time(0));
  return (rand() % (upper - lower + 1)) + lower;
}

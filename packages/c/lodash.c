#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Date

int now() {
  time_t seconds = time(NULL);
  return seconds;
}

// Lang

bool gt(float value, float other) {
  return value > other;
}

bool gte(float value, float other) {
  return value >= other;
}

bool lt(float value, float other) {
  return value < other;
}

bool lte(float value, float other) {
  return value <= other;
}

// Math

float add(float a, float b) {
  return a + b;
}

float divide(float a, float b) {
  return a / b;
}

float multiply(float a, float b) {
  return a * b;
}

float subtract(float a, float b) {
  return a - b;
}

// Number

float clamp(float number, float lower, float upper) {
  if (lower > upper) {
    float temp = lower;
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

bool inRange(float number, float start, float end) {
  if (start > end) {
    float temp = end;
    end = start;
    start = temp;
  }
  return start < number && number < end;
}

int randomNumber(int lower, int upper) {
  if (lower > upper) {
    int temp = lower;
    lower = upper;
    upper = temp;
  }
  srand(time(0));
  return (rand() % (upper - lower + 1)) + lower;
}

// String 

bool endsWith(char * string, char target, int position) {
  return string[strlen(string) - position] == target;
}

bool startsWith(char * string, char target, int position) {
  return string[position] == target;
}

char* toLower(char* string) {
  for(char *p = string; *p; p++) *p=tolower(*p);
  return string;
}

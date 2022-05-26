#include "lodash.h"
#include <stdio.h>

void testDate();
void testLang();
void testMath();
void testNumber();
void testString();

int main() {
  testDate();
  testLang();
  testMath();
  testNumber();
  testString();

  return 0;
}

void testDate() {
  // now
  int nowTimestamp = now();
  printf("%d\n", nowTimestamp);
}

void testLang() {
	// gt
	bool greaterThan1 = gt(3, 1);
	bool greaterThan2 = gt(3, 3);
  if (greaterThan1 && !greaterThan2) {
    printf("gt true\n");
  }
	// gte
	bool greaterThanOrEqual1 = gte(3, 1);
	bool greaterThanOrEqual2 = gte(3, 3);
  if (greaterThanOrEqual1 && greaterThanOrEqual2) {
    printf("gte true\n");
  }
	// lt
	bool lessThan1 = lt(1, 3);
	bool lessThan2 = lt(3, 3);
  if (lessThan1 && !lessThan2) {
  	printf("lt true\n");
  }
	// lte
	bool lessThanOrEqual1 = lte(1, 3);
	bool lessThanOrEqual2 = lte(3, 3);
  if (lessThanOrEqual1 && lessThanOrEqual2) {
    printf("lte true\n");
  }
}

void testMath() {
  // add
  float total = add(6, 4);
  printf("add %s\n", total == 10 ? "true" : "false");
  // divide
  float quotient = divide(6, 4);
  printf("divide %s\n", quotient == 1.5 ? "true" : "false");
  // multiply
  float product = multiply(6, 4);
  printf("multiply %s\n", product == 24 ? "true" : "false");
  // subtract
  float difference = subtract(6, 4);
  printf("subtract %s\n", difference == 2 ? "true" : "false");
}

void testNumber() {
  // clamp
  float clamped1 = clamp(-10, -5, 5);
  float clamped2 = clamp(10, -5, 5);
  if (clamped1 == -5 && clamped2 == 5) {
    printf("clamp true\n");
  }
  // inRange
  bool inRange1 = inRange(3, 2, 4);
  bool inRange2 = inRange(-3, -2, -6);
  bool inRange3 = inRange(4, 0, 2);
  bool inRange4 = inRange(2, 0, 2);
  if (inRange) {
    printf("inRange true\n");
  }
  // random
  int random1 = randomNumber(0, 5);
  int random2 = randomNumber(5, 10);
  if (0 <= random1 && random1 <= 5 && 5 <= random2 && random2 <= 10) {
    printf("randomNumber true\n");
  }
}

void testString() {
  // endsWith
  bool endsWithT = endsWith("test", 't', 1);
  printf("endsWith %s\n", endsWithT ? "true" : "false");
  // startsWith
  bool startsWithT = startsWith("test", 't', 0);
  printf("startsWith %s\n", startsWithT ? "true" : "false");
  // toLower
  char* lower = toLower("TEST");
  printf("toLower %s\n", lower == "test" ? "true" : "false");
}

#include <time.h>
#include "iostream"
#include "lodash.hpp"

using namespace std;

void testArray();
void testLang();
void testMath();
void testNumber();

int main() {
  testArray();
  testLang();
  testMath();
  testNumber();

  return 0;
}

void testArray() {
  // head
  int headArray1[] = {1, 2, 3};
  int headArray2[] = {4, 5, 6};
  int head1 = head(headArray1);
  int head2 = head(headArray2);
  if (head1 == 1 && head2 == 4) {
    cout << "head true" << "\n";
  }
  // last
  int lastArray1[3] = {1, 2, 3};
  int lastArray2[3] = {4, 5, 6};
  int last1 = last(lastArray1, 3);
  int last2 = last(lastArray2, 3);
  if (last1 == 3 && last2 == 6) {
    cout << "last true" << "\n";
  }
  // nth
  int nArray[6] = {1, 2, 3, 4, 5, 6};
  int nth1 = nth(nArray, 1, 6);
  int nth2 = nth(nArray, -2, 6);
  if (nth1 == 2 && nth2 == 3) {
    cout << "nth true" << "\n";
  }
}

void testLang() {
  // gt
	bool greaterThan1 = gt(3, 1);
	bool greaterThan2 = gt(3, 3);
  if (greaterThan1 && !greaterThan2) {
    cout << "gt true" << "\n";
  }
	// gte
	bool greaterThanOrEqual1 = gte(3, 1);
	bool greaterThanOrEqual2 = gte(3, 3);
  if (greaterThanOrEqual1 && greaterThanOrEqual2) {
    cout << "gte true" << "\n";
  }
	// lt
	bool lessThan1 = lt(1, 3);
	bool lessThan2 = lt(3, 3);
  if (lessThan1 && !lessThan2) {
    cout << "lt true" << "\n";
  }
	// lte
	bool lessThanOrEqual1 = lte(1, 3);
	bool lessThanOrEqual2 = lte(3, 3);
  if (lessThanOrEqual1 && lessThanOrEqual2) {
    cout << "lte true" << "\n";
  }
}

void testMath() {
  // add
  float total = add(6, 4);
  if (total == 10) {
    cout << "add true" << "\n";
  }
  // divide
  float quotient = divide(6, 4);
  if (quotient == 1.5) {
    cout << "divide true" << "\n";
  }
  // multiply
  float product = multiply(6, 4);
  if (product == 24) {
    cout << "multiply true" << "\n";
  }
  // substract
  float difference = subtract(6, 4);
  if (difference == 2) {
    cout << "subtract true" << "\n";
  }
}

void testNumber() {
  // clamp
  float clamped1 = clamp(-10, -5, 5);
  float clamped2 = clamp(10, -5, 5);
  if (clamped1 == -5 && clamped2 == 5) {
    cout << "clamp true" << "\n";
  }
  // inRange
  bool inRange1 = inRange(3, 2, 4);
  bool inRange2 = inRange(-3, -2, -6);
  bool inRange3 = inRange(4, 0, 2);
  bool inRange4 = inRange(2, 0, 2);
  if (inRange1 && inRange2 && !inRange3 && !inRange4) {
    cout << "inRange true" << "\n";
  }
  // random
  int random1 = random(0, 5);
  int random2 = random(5, 10);
  if (0 <= random1 && random1 <= 5 && 5 <= random2 && random2 <= 10) {
    cout << "random true" << "\n";
  }
}
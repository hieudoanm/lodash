#include <stdbool.h>
// Date
int now();
// Lang
bool gt(float value, float other);
bool gte(float value, float other);
bool lt(float value, float other);
bool lte(float value, float other);
// Math
float add(float a, float b);
float divide(float a, float b);
float multiply(float a, float b);
float subtract(float a, float b);
// Number
float clamp(float number, float lower, float upper);
bool inRange(float number, float start, float end);
int randomNumber(int lower, int upper);
// String
bool endsWith(char * string, char target, int position);
bool startsWith(char * string, char target, int position);
char * toLower(char * string);
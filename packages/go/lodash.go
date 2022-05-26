package main

import (
	"fmt"
	"math"
	"math/rand"
	"strings"
	"time"
)

func main() {
	testArray();
	testDate();
	testLang();
	testMath();
	testNumber();
	testString();
	testUtil();
}

func testArray() {
	// indexOf
	var _indexOf1 int = indexOf([]float64{1, 2, 1, 2}, 2, 0);
	var _indexOf2 int = indexOf([]float64{1, 2, 1, 2}, 2, 2);
	if (_indexOf1 == 1 && _indexOf2 == 3) {
		fmt.Println("indexOf true");
	}
	// lastIndexOf
	var _lastIndexOf1 int = lastIndexOf([]float64{1, 2, 1, 2}, 2, 0);
	var _lastIndexOf2 int = lastIndexOf([]float64{1, 2, 1, 2}, 2, 2);
	if (_lastIndexOf1 == 3 && _lastIndexOf2 == 1) {
		fmt.Println("lastIndexOf true");
	}
}

func testDate() {
	// now
	var nowTS int64 = now();
	fmt.Println("now", nowTS);
}

func testLang() {
	// gt
	var greaterThan1 bool = gt(3, 1)
	var greaterThan2 bool = gt(3, 3)
	if greaterThan1 && !greaterThan2 {
		fmt.Println("gt true")
	}
	// gte
	var greaterThanOrEqual1 bool = gte(3, 1)
	var greaterThanOrEqual2 bool = gte(3, 3)
	if greaterThanOrEqual1 && greaterThanOrEqual2 {
		fmt.Println("gte true")
	}
	// lt
	var lessThan1 bool = lt(1, 3)
	var lessThan2 bool = lt(3, 3)
	if lessThan1 && !lessThan2 {
		fmt.Println("lt true")
	}
	// lte
	var lessThanOrEqual1 bool = lte(1, 3)
	var lessThanOrEqual2 bool = lte(3, 3)
	if lessThanOrEqual1 && lessThanOrEqual2 {
		fmt.Println("lte true")
	}
}

func testMath() {
	// add
	var total float64 = add(6, 4)
	fmt.Println("add", total == 10)
	// ceil
	var roundedUp float64 = ceil(4.006)
	fmt.Println("ceil", roundedUp == 5)
	// divide
	var quotient float64 = divide(6, 4)
	fmt.Println("divide", quotient == 1.5)
	// floor
	var roundedDown float64 = floor(4.006)
	fmt.Println("floor", roundedDown == 4)
	// max
	var maximum float64 = max([]float64{4, 2, 8, 6})
	fmt.Println("max", maximum == 8)
	// mean
	var _mean float64 = mean([]float64{4, 2, 8, 6})
	fmt.Println("mean", _mean == 5)
	// min
	var minimum float64 = min([]float64{4, 2, 8, 6})
	fmt.Println("min", minimum == 2)
	// multiply
  var product float64 = multiply(6, 4)
  fmt.Println("multiply", product == 24)
	// round
	var rounded1 float64 = round(4.1)
	var rounded2 float64 = round(4.9)
	if rounded1 == 4 && rounded2 == 5 {
		fmt.Println("round true")
	}
	// subtract
	var difference float64 = subtract(6, 4)
	fmt.Println("subtract", difference == 2)
	// sum
	var _sum float64 = sum([]float64{4, 2, 8, 6})
	fmt.Println("sum", _sum == 20)
}

func testNumber() {
	// clamp
  var clamped1 float64 = clamp(-10, -5, 5)
  var clamped2 float64 = clamp(10, -5, 5)
	if clamped1 == -5 && clamped2 == 5 {
	  fmt.Println("clamped true")
	}
	// inRange
	var inRange1 bool = inRange(3, 2, 4)
	var inRange2 bool = inRange(4, 0, 8)
	var inRange3 bool = inRange(4, 0, 2)
	var inRange4 bool = inRange(2, 0, 2)
	if inRange1 && inRange2 && !inRange3 && !inRange4 {
	  fmt.Println("isRange true")
	}
 	// random
	var random1 = random(0, 5)
	var random2 = random(5, 10)
	if 0 < random1 && random1 < 5 && 5 < random2 && random2 < 10 {
		fmt.Println("random true")
	}
}

func testString() {
	// endsWith
	var _endsWith1 bool = endsWith("abc", 'c', 1)
	var _endsWith2 bool = endsWith("abc", 'b', 1)
	var _endsWith3 bool = endsWith("abc", 'b', 2)
	if (_endsWith1 && !_endsWith2 && _endsWith3) {
		fmt.Println("endsWith true")
	}
	// trim
	var _trim string = trim("  abc  ", " ")
	fmt.Println("trim", _trim == "abc")
	// trimEnd
	var _trimEnd string = trimEnd("  abc  ", " ")
	fmt.Println("trimEnd", _trimEnd == "  abc")
	// trimStart
	var _trimStart string = trimStart("  abc  ", " ")
	fmt.Println("trimStart", _trimStart == "abc  ")
	// startsWith
	var _startsWith1 bool = startsWith("abc", 'a', 0)
	var _startsWith2 bool = startsWith("abc", 'a', 1)
	var _startsWith3 bool = startsWith("abc", 'b', 1)
	if (_startsWith1 && !_startsWith2 && _startsWith3) {
		fmt.Println("startsWith true")
	}
}

func testUtil() {
	// stubArray
	var _stubArray [0]int = stubArray()
	fmt.Println("stubArray", _stubArray == [0]int{})
	// stubFalse
	var _stubFalse bool = stubFalse()
	fmt.Println("stubFalse", !_stubFalse)
	// stubString
	var _stubString string = stubString()
	fmt.Println("stubString", _stubString == "")
	// stubTrue
	var _stubTrue bool = stubTrue()
	fmt.Println("stubTrue", _stubTrue)
}

// Array

func indexOf(array []float64, value float64, fromIndex int) int {
	var slice []float64 = array[fromIndex:]
  for idx, v := range slice {
    if v == value {
      return idx + fromIndex
    }
	}
  return -1
}

func lastIndexOf(array []float64, value float64, fromIndex int) int {
	var index int = -1;
	var slice []float64 = array[0:len(array) - fromIndex];
  for idx, v := range slice {
    if v == value {
      index = idx;
    }
	}
  return index;
}

// Date

func now() int64 {
	var now time.Time = time.Now();
	var sec int64 = now.Unix()
	return sec;
}

// Lang

func gt(value float64, other float64) bool {
	return value > other
}

func gte(value float64, other float64) bool {
	return value >= other
}

func lt(value float64, other float64) bool {
	return value < other
}

func lte(value float64, other float64) bool {
	return value <= other
}

// Math

func add(a float64, b float64) float64 {
	return a + b
}

func ceil(number float64) float64 {
	return math.Ceil(number)
}

func divide(a float64, b float64) float64 {
	return a / b
}

func floor(number float64) float64 {
	return math.Floor(number)
}

func max(array []float64) float64 {
	var maximum float64 = math.Inf(-8);
	for i := 0; i < len(array); i++ {
		var number float64 = array[i];
		if number > maximum {
			maximum = number
		}
	}
	return maximum
}

func mean(array []float64) float64 {
	if len(array) == 0 {
		return 0
	}
	var _sum float64 = sum(array)
	var mean float64 = _sum / float64(len(array))
	return mean
}

func min(array []float64) float64 {
	var minimum float64 = math.Inf(8);
	for i := 0; i < len(array); i++ {
		var number float64 = array[i];
		if number < minimum {
			minimum = number
		}
	}
	return minimum
}

func multiply(a float64, b float64) float64 {
	return a * b
}

func round(number float64) float64 {
	return math.Round(number)
}

func subtract(a float64, b float64) float64 {
	return a - b;
}

func sum(array []float64) float64 {
	var sum float64 = 0
	for i := 0; i < len(array); i++ {
		var number float64 = array[i];
		sum += number
	}
	return sum
}

// Number

func clamp(number float64, lower float64, upper float64) float64 {
	if number < lower {
		return lower
	}
	if number > upper {
		return upper
	}
	return number
}

func inRange(params ...float64) bool {
	if len(params) == 2 {
		var number float64 = params[0];
		var stop float64 = params[1];
		return 0 < number && number < stop;
	}

	if len(params) >= 3 {
		var number float64 = params[0];
		var start float64 = params[1];
		var stop float64 = params[2];
		return start < number && number < stop;
	}

	return false
}

func random(lower int, upper int) int {
  if (lower > upper) {
    var temp int = lower;
    lower = upper;
    upper = temp;
  }
	return rand.Intn(upper - lower) + lower;
}

// String

func endsWith(str string, char byte, position int) bool {
	var lastIndex int = len(str) - position
	return str[lastIndex] == char;
}

func trim(str string, chars string) string {
	return strings.Trim(str, chars)
}

func trimEnd(str string, chars string) string {
	return strings.TrimRight(str, chars)
}

func trimStart(str string, chars string) string {
	return strings.TrimLeft(str, chars)
}

func startsWith(str string, char byte, position int) bool {
	return str[position] == char;
}

// Util

func stubArray() [0]int {
	var array = [0]int{}
	return array
}

func stubFalse() bool {
	return false
}

func stubString() string {
	return ""
}

func stubTrue() bool {
	return true
}

// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

contract Lodash {
    // Lang
    function gt(uint a, uint b) public pure returns(bool) {
        return a > b;
    }
    
    function gte(uint a, uint b) public pure returns(bool) {
        return a >= b;
    }
    
    function lt(uint a, uint b) public pure returns(bool) {
        return a < b;
    }
    
    function lte(uint a, uint b) public pure returns(bool) {
        return a <= b;
    }
    // Math
    function add(uint a, uint b) public pure returns(uint) {
        return a + b;
    }

    function divide(uint a, uint b) public pure returns(uint) {
        return a / b;
    }

    function multiply(uint a, uint b) public pure returns(uint) {
        return a * b;
    }

    function subtract(uint a, uint b) public pure returns(uint) {
        return a - b;
    }
    // Number
    function clamp(uint number, uint lower , uint upper) public pure returns(uint) {
        if (lower > upper) {
            return lower;
        }  
        if (number < lower) {
            return lower;
        }
        if (number > upper) {
            return upper;
        }
        return number;
    }

    function inRange(uint number, uint start, uint end) public pure returns(bool) {
        return start < number && number < end;
    }
}

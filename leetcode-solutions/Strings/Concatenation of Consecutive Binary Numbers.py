"""Concatenation of Consecutive Binary Numbers
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.
Problem Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/?envType=daily-question&envId=2026-02-28"""

def concatenatedBinary( n: int) -> int:
        res_string=""
        for i in range(1,n+1):
            res_string = res_string + bin(i)[2:]  
        return int(res_string,2) % (7+10**9)
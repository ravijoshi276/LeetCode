"""Complement of Base 10 Integer

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

Problem Link: https://leetcode.com/problems/complement-of-base-10-integer/?envType=daily-question&envId=2026-03-11"""

def bitwiseComplement(n: int) -> int:
        pow =0
        num=2**0
        if n==0:
            return 1 
        while(num<=n):
            num=2**pow
            pow+=1
        
        return ~n & (num-1)
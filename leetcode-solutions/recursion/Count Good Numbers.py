"""Count Good Numbers

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.
Problem Link: https://leetcode.com/problems/count-good-numbers/"""

#Solve power(x,n) before solving this

def countGoodNumbers(n: int) :
        if n ==1:
            return 5
        else:
            odd = n//2 
            even = n - odd
            def binary_exponent(base,exponent,mod=(10**9+7)):
                res=1
                while(exponent>0):
                    if exponent &1 : # Same as n %2 ==1
                        res *=base
                    base = (base*base)%mod
                    exponent >>=1 #Same as n//2
                return res 

            return (binary_exponent(5,even)*binary_exponent(4,odd)) %(10**9+7)

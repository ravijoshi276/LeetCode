"""Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Problem Link : https://leetcode.com/problems/powx-n/"""

def myPow(x: float, n: int) :
        if n==0:
            return 1
        if n < 0:
            x = 1/x
            n=-n
        res =1
        while(n!=0):
            if n %2 ==1:
                res*=x
            x*=x
            n=n//2
        return res
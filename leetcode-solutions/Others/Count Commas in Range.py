"""Count Commas in Range

You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.
Problem Link: https://leetcode.com/problems/count-commas-in-range/description/"""

def countCommas( n: int) :
        if n <1000:
            return 0
        comma=0
        places=0
        temp =n
        while(n>0):
            places+=1
            n= n//10
            if n >0 and places>=3:
                comma = temp -(10**(3*(places//3))) +1
            
        return comma
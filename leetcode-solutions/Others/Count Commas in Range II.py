"""Count Commas in Range II

You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

A comma is inserted after every three digits from the right.
Numbers with fewer than 4 digits contain no commas.

Problem Link: https://leetcode.com/problems/count-commas-in-range-ii/"""

def countCommas(n: int):
    if n <1000:
        return 0
    comma=0
    places=0
    temp =n
    while(n>0):
        p=places//3
        places+=1
        n= n//10
        if n  and p != places//3:
            comma += temp - (10**(3*(p+1))) +1
    return comma
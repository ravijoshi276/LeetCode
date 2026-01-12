"""1614. Maximum Nesting Depth of the Parentheses

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
Problem Link : https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/


Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

"""

def maxDepth(s: str) :
    """Code Start"""
    count = 0 # Count of depth
    res = 0 # Stores the maximum
    for i in s:
        if i == "(":
            count +=1
        elif i == ')':
            count -=1
        res = max(res,count)
    
    return res

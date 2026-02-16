"""Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type

Problem link: https://leetcode.com/problems/valid-parentheses/?envType=problem-list-v2&envId=string
"""
"""
Logic : A dictionary to match closing bracket to opeaning.

"""

def isValid(s: str):
        if len(s)==0 or len(s)%2==1:
            return False
        mpp_close = {']':'[','}':'{',')':"("}
        mpp_open={}
        for k,v in mpp_close.items():
            mpp_open[v]=k
        lst= []
        for i in s:
            if i in mpp_open:
                lst.append(i)
            else:
                if len(lst) and lst[-1] == mpp_close[i] :
                    lst.pop()
                else:
                    return False

        if len(lst)==0:
            return True
        return False 
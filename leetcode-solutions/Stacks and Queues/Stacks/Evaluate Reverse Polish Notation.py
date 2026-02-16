"""Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Problem Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=problem-list-v2&envId=dsa-linear-shoal-stack
"""


#Logic
#--> Store number in stack space and as soon as we find a special character we perform that action
def evalRPN(tokens: list[str]):
    s  = []
    n = len(tokens)
    sym = {"+","-","*","/"}
    for i in range(n):
        if tokens[i] not in sym:
            s.append(int(tokens[i]))
        
        else:
            
            first = s.pop()
            second = s.pop()
            if tokens[i]=="+":
                res = first+second
            elif tokens[i] == "-":
                res = second-first
            elif tokens[i]=="*":
                res = second *first
            else :
                res = second/first
            s.append(int(res))
        return s[0] #returning s[0] in case where there is just one input
        
    
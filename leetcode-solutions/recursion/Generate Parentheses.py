"""Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Problem Link: https://leetcode.com/problems/generate-parentheses/"""

def generateParenthesis( n: int) :
    lst=[]
    
    def generate(l,r,s,n,res):
        if len(s) == 2*n:
            lst.append(s)
            return
        if l < n:
            generate(l+1,r,s+'(',n,res)
        if r<l:
            generate(l,r+1,s + ')',n,res)
        
        
    generate(0,0,"",n,lst)
    return lst


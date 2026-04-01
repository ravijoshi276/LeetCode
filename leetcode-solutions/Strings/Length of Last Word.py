"""Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
Problem Link: https://leetcode.com/problems/length-of-last-word/description/?envType=problem-list-v2&envId=string
"""

def lengthOfLastWord(s: str) -> int:
        s = s.strip()
        n = len(s)
        j = n-1
        if n ==0:
            return ""
        while j>=0 and (s[j]!=" "):
            j-=1
        
        return n-j-1
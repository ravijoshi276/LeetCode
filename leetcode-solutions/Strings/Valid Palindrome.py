"""125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise

Problem Link : https://leetcode.com/problems/valid-palindrome/description/

Input: s = "A man, a plan, a canal: Panama"
Output: true
"""

def isPalindrome(s: str):
    s = s.lower()
    start= 0 # Start pointer
    end = len(s)-1 # End Pointer
    while(start<end):
        while(start< end and not s[start].isalnum()): #Search till we find valid alphabet or number
            start+=1
        while(start<end and not s[end].isalnum()):
            end-=1
        if s[start]!=s[end]: # CAse where two pointers do not match
            return False    
        start+=1 #Case when they match
        end-=1
    return True
"""
Logic:
This is a two pointer approach:
One point on the start and other on the end
Search till we find a valid alphabet of number.
Match start with end.
If start == end we continue
else return false
"""
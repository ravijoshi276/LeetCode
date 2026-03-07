"""Minimum Number of Flips to Make the Binary String Alternating

You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Problem Link: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/?envType=daily-question&envId=2026-03-07"""

def minFlips( s: str) :
        start_0=0
        n=len(s)
        ans = n
        t = s+s
        
        for i in range(2*n):
            expected = "0" if i %2 ==0 else "1"
            
            if expected==t[i]:
                start_0+=1
    
            if i >=n:
                left = i-n
                exp_left = "0" if left %2 ==0 else "1"
                if t[left] == exp_left:
                    start_0-=1
            if i >=n-1:
                start_1 = n -start_0
                ans = min(start_0,start_1,ans)
        
        return ans
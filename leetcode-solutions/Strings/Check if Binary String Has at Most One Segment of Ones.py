"""Check if Binary String Has at Most One Segment of Ones

Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 
Problem link : https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/?envType=daily-question&envId=2026-03-06"""


def checkOnesSegment(s: str) :
        flag = False
        n = len(s)
        if n==1 and s[0]=="1":
            flag=True
        for i in range(1,n):
            if (s[i]=="1" or s[i-1]=="1") and flag==False:
                flag = True
            elif s[i]=="1" and s[i-1]=='0':
                flag=False
                break
        return flag
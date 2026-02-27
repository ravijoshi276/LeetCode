"""Count Binary Substrings

Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
Problem link : https://leetcode.com/problems/count-binary-substrings/?envType=daily-question&envId=2026-02-19"""

"""Optimized solution
as we just need count complexity O(N)
"""
def countBinarySubstrings(s):
    res =0
    counter =1
    temp=0
    n = len(s)
    for i in range(1,n):
        if s[i]==s[i-1]:
            counter+=1
        else:
            temp =counter
            counter=1
        if counter<= temp:
             res+=1
    return res



"""Brute Force approach"""
def countBinarySubstrings(s: str) :
        p1 =0
        p2 = 0
        mpp = {'1':0,'0':0}
        res =0
        n = len(s)
        while(p1<n and p2<n):
            while(p2<n and s[p2]==s[p1]):
                mpp[s[p2]]+=1
                p2+=1
            temp =p2
            while(p2<n and s[p2]==s[temp] ):
                mpp[s[p2]]+=1
                p2+=1
    
            res+= min(mpp.values())
            mpp.clear()
            mpp = {'1':0,'0':0}
            p1=temp
            p2=p1
            
            
         
        return res
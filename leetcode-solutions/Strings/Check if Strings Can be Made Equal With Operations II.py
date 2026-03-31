"""Check if Strings Can be Made Equal With Operations II

You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

Problem Link: https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/?envType=daily-question&envId=2026-03-31"""

def checkStrings( s1: str, s2: str) -> bool:
        n = len(s1)
        mpp ={}
        mpp2={}
        if s1==s2:
            return True
        for i in range(0,n,2):
                mpp[s1[i]]= mpp.get(s1[i],0)+1
                mpp2[s2[i]]= mpp2.get(s2[i],0)+1
        if mpp!=mpp2:
            return False
        mpp.clear()
        mpp2.clear()
        for i in range(1,n,2):
                mpp[s1[i]]= mpp.get(s1[i],0)+1
                mpp2[s2[i]]= mpp2.get(s2[i],0)+1
        if mpp!=mpp2:
            return False
        return True
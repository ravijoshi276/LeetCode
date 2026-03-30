"""Check if Strings Can be Made Equal With Operations I

You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.
Problem Link : https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/?envType=daily-question&envId=2026-03-30"""
def canBeEqual(s1: str, s2: str) -> bool:
        if s1 ==s2: return True
        for i in range(4):
            if s1[i] != s2[i]:
                if i >=2 and s1[i]==s2[i-2] and s2[i]==s1[i-2]:
                    continue
                elif i < 2 and s1[i]==s2[i+2] and s2[i]==s1[i+2]:
                    continue
                else:
                    return False
        
        return True
    
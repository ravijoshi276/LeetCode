"""Longest Balanced Substring I

You are given a string s consisting of lowercase English letters.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

Problem Link :https://leetcode.com/problems/longest-balanced-substring-i/?envType=daily-question&envId=2026-02-12
"""

def longestBalanced(s: str) -> int:
        n = len(s)
        if n ==0 or n==1: #case when empty string or single character
            return n
        m = -1
        for i in range(n):
            mpp ={} # to store the frequency during each loop
            for j in range(i,n):
                mpp[s[j]] = mpp.get(s[j],0)+1
            
                if len(set(mpp.values())) ==1: # The set of values will be 1 if each values are same.
                    m = max(m,j-i+1)
            if m ==n : # case when we get m ==n in the very first loop
                break
        
        return m

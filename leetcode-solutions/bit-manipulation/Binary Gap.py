"""Binary Gap

Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

Problem Link : https://leetcode.com/problems/binary-gap/description/?envType=daily-question&envId=2026-02-22
"""

def binaryGap( n: int) -> int:
        b = bin(n)[2:]
        n = len(b)
        p=0
        m =0
        while(p<n and b[p]!='1'):
            p+=1
        
        for i in range(p,n):
            if b[i]=='1':
                m = max(i-p,m)
                p=i
        
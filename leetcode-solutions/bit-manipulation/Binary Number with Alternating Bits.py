"""Binary Number with Alternating Bits


Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Problem Link : https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18
"""

def hasAlternatingBits( n: int) -> bool:
        x = n
        res=True
        while(x>0):
            next_x= x//2
            if (x%2 is 0 and next_x %2 ==1) or ( x%2 is 1 and next_x %2 ==0):
                x = next_x
            else:
                res = False
                break
        return res
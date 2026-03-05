"""Minimum Changes To Make Alternating Binary String

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.

Problem Link : https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/?envType=daily-question&envId=2026-03-05"""

def minOperations(s: str):
        n = len(s)
        if n<=1 :
            return 0
        count_0=0
        count_1=0
        flag=0
        for i in range(n):
            if flag==0:
                if s[i] != "0":
                    count_0+=1
                else:
                    count_1+=1
            else:
                if s[i]!="1":
                    count_0+=1
                else:
                    count_1+=1
            flag ^=1
        
       
        
        return min(count_0,count_1) 
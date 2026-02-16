"""Longest Balanced Substring II

You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.

Problem link: https://leetcode.com/problems/longest-balanced-substring-ii/?envType=daily-question&envId=2026-02-13"""
def longestBalanced( s: str) :
        n = len(s)
        """
        list to store the prefix sum of 'abc'
        we will be storing the count of a b and c
        """
        p_sum =[[0,0,0]]
        for i in range(n):
            current_sum = p_sum[-1][:] #copy of previous sum
            current_sum["abc".index(s[i])]+=1
            p_sum.append(current_sum)
        """
        Declaring a hash map for condition check and condition match
        There will be 7 condions to check for:
        ('a',a-b,b-c) #When a==b==c (all are equal or all are zero)
        ('b',a-b,c) # When a==b and c is zero
        ('c',a-c,b) # When a==c and b is zero
        ('d',b-c,a) #When c ==b and a is zero
        ('e',a,b) # when a and b are zero
        ('f'a,c) # when b is zero
        ('g',b,c) #When a is zero
        """
        
        mpp={} # to store the first instance of condition match
        m=0 #Stores the maximum
        """Now enumerating so that first index along with the values can be stored. Alternatively we can use len"""
        
        for index,(a,b,c) in enumerate(p_sum):
            conditions = [('a',a-b,b-c),('b',a-b,c),('c',a-c,b),('d',b-c,a),('e',a,b),('f',a,c),('g',b,c)]
            for k in conditions:
                if not k in mpp:
                    mpp[k]=index
                else:
                    m = max(m,index-mpp[k])
        
        
        return m
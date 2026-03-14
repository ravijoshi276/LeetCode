""" The k-th Lexicographical String of All Happy Strings of Length n

A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Problem Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2026-03-14"""
"""Logic

Generate all the string
Find the kth term after sorting 
"""
def getHappyString(n: int, k: int):
        lst=[]
        def genereate_strings(n,characters,string):
            if n ==0:
                lst.append(string)
                return
            
            for char in characters:
                if len(string)>=1 and char ==string[-1]:
                    continue
                new_s = string+ char
                genereate_strings(n-1,characters,new_s)
        
        genereate_strings(n,"abc","")
        lst.sort()
        if k > len(lst):
            return ""
        return lst[k-1]
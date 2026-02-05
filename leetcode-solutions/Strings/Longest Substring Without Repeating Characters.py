""" Longest Substring Without Repeating Characters


Problem Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
## Logic
"""
Step 1
    We store all the non repeating elements in a data structure.
Step 2 
    As soon as we find the repeating element. We compare the length of data structure with current maximum.
    We also remove all the elements till the repeating element that matches the element at current index. (Similar to sliding window)

"""

s = "abcabcbb"
def lengthOfLongestSubstring(self, s: str) -> int:
        a = set() # Stores the non repeating elements
        m = -1 #Strores the maximum length
        p = 0 # Pointer 
        n = len(s)
        for i in range(n):
            if s[i] not in a:
                a.add(s[i])
            else:
    
                m = max(m,len(a))
               
                for j in range(p,n):
                    if s[j] == s[i]:
                        p = j+1
                        break
                    a.remove(s[j])
                    
        m = max(m, len(a))

        return m

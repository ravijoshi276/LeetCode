'''Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

problem link : https://leetcode.com/problems/reverse-words-in-a-string/

Input: s = "the sky is blue"
Output: "blue is sky the"
'''

s = "the sky is blue"
def reverseWords(s):
    n = len(s)-1
    start = n
    end = n
    res = ""
    while(start>=0):
        if s[start] == " " and  start != n and s[start+1] != " ":
            res += s[start+1 : end+1].strip() + " " 
            end = start
        elif s[start] != " " and start != n and s[start+1] == " ":
            end = start+1
        if start == 0:
            t = s[start:end+1].strip()
            res += t
        start-=1
    
    return res.strip()
x = reverseWords(s)
print(x)
s ="  hello world  "
x = reverseWords(s)
print(x)
x.strip()
print(x)

"""
Logic:
1. We start by looking from end of string.
2. As soon as we find a space and the element next to it is not space.We add the element to result
3. we update the end as soon as we find an element whose next element is space.
4. When the string reaches 0 we add the remaining string to the result and trim it
"""
"""451. Sort Characters By Frequency
problem description
Given a string s, 
sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

"""

def frequencySort(s):
    d = {}#Creating a hash map of frequency of characters
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    sorted_d =sorted(d.items(),key = lambda x: x[1],reverse=True)# Creating a sorted list on the basis of frequency
    res = ""# Created a string to return result
    for i in range(len(sorted_d)):
        res += str(sorted_d[i][0]) * sorted_d[i][1] #Concatinated the sting for returning
    return res
s = "tree"
x = frequencySort(s)
print(x)            


"""
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

link : https://leetcode.com/problems/sort-characters-by-frequency/submissions/1870019291/"""
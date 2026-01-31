"""Find Smallest Letter Greater Than Target

You are given an array of characters letters that is sorted in non-decreasing order, and a character target. 
There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Problem Link:https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/?envType=daily-question&envId=2026-01-31
"""
def nextGreatestLetter(letters: list[str], target: str):
    start = 0
    end = len(letters)-1
    while(start<=end):
        mid = (start+end)//2
        if letters[mid]<= target:
            start = mid+1
        else:
            end = mid-1
    
    return letters[start%len(letters)]

"""
Logic : We will do a simple binary search.

    edge case: when start exceeds the end or value of start is equal to number of elements in array.
    solution : we return the first element in the array.

"""
"""Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
problem link : https://leetcode.com/problems/binary-search/description/

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""
def search(nums: list[int],target: int):
    start = 0
    end = len(nums)-1 #start and end of search
    while(start<=end):
        mid = (start+end)//2 # floor division
        if nums[mid]==target:
            return mid
        elif nums[mid]< target:
            start= mid +1
        else:
            end = mid -1
    
    return -1 # if target not found 

"""
Approach : We select a middle index.
    There can be 3 cases :
        1. Either the target is greater (In this case we look at the right of index )
        2. Target is smaller ( In this case we look to the left of index )
        3 Target is equal ( In this case we return )
"""
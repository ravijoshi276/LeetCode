"""35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Problem Link : https://leetcode.com/problems/search-insert-position/description/

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
def searchInsert( nums, target):
    start = 0
    end = len(nums)-1
    while(start<=end):
        mid = (start+ end)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]< target:
            start = mid +1
        else:
            end = mid -1
    
    return start
"""
Logic : 
We Perform binary search till we find element or else return start 
"""
"""
Link to problem :https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

1752. Check if Array Is Sorted and Rotated
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

Input: nums = [3,4,5,1,2]
Output: true
"""
def check(nums:list[int]):# Input is list of integer
    count = 0 
    #Setting a count as a flag to check the instance where a numver is less than the following number
    n = len(nums) #length of nums
    for i in range(n):
        if nums[i]> nums[(i+1) % n]: #checking the last element with first element
            count +=1
    if count >1:
        return False
    return True

nums = [3,4,5,1,2]
print(check(nums))

"""
Logic : if the array is sorted there will be exactly one instance 
        where a number is greater than the following number
"""

"""Rotating an array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

link : https://leetcode.com/problems/rotate-array/description/
"""

nums = [1,2,3,4,5,6,7] #input
k = 3
# Rotate a list k position to the right without using extra space
def rotate ( nums,k):
   nums[:] = nums[::-1] #reversing the list ; output :[7, 6, 5, 4, 3, 2, 1]
   print(nums)
   nums[:k] = nums[:k][::-1] # reversing the first 3 eleement ; output : [5, 6, 7, 4, 3, 2, 1]
   print(nums)
   nums[k:] = nums[k:][::-1] #reversing rest of elements ; output : [5, 6, 7, 1, 2, 3, 4]

rotate ( nums,k) #function call
print(nums) #printing to check result



nums = [1,2,3,4,5,6,7]
# Using extra space

def rotate_k(nums,k):
    n = len(nums)
    result = [0 for i in range(n) ]
    for i in range(k):
        result[i] = nums[n-k+i]
    for i in range(k,n):
        result[i] = nums[i-k]

    return result #returning statement 

x = rotate_k(nums,k)
print(x)
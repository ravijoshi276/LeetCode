"""Find the Smallest Balanced Index

You are given an integer array nums.

An index i is balanced if the sum of elements strictly to the left of i equals the product of elements strictly to the right of i.

If there are no elements to the left, the sum is considered as 0. Similarly, if there are no elements to the right, the product is considered as 1.

Return an integer denoting the smallest balanced index. If no balanced index exists, return -1.

Problem Link : https://leetcode.com/problems/find-the-smallest-balanced-index/"""

def smallestBalancedIndex(nums: list[int]) :
    s= sum(nums)
    n = len(nums)-1
    pro = 1

    for i in range(n,-1,-1):
        s-= nums[i]
        if s==pro:
            return i
        elif pro > s:
            break
        pro *= nums[i]
    
    return -1
    
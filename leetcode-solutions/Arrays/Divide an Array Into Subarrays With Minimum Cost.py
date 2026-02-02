
"""Divide an Array Into Subarrays With Minimum Cost I

You are given an array of integers nums of length n.

The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

You need to divide nums into 3 disjoint contiguous subarrays.

Return the minimum possible sum of the cost of these subarrays.

Problem link :https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/?envType=daily-question&envId=2026-02-01
"""

#Approch 1 
"""
The mininum of first element + 2 minimum elements

Time complexity : On 
Space complexity : O1
"""
def minimumCost(nums: list[int]):
    a = nums[0] # First element
    n = len(nums)
    mini = nums[1] # Minimum element
    mini_2 = None # 2 nd smallest element
    for i in range(2,n):
        if nums[i]< mini: # When we find a lower number than minimum
            mini_2 = mini
            mini = nums[i]
        elif mini_2 is None or mini_2>nums[i]>=mini: #When we find a number greater of equal to minimum but smaller than the 2nd smallest
            mini_2 = nums[i]
    
    return a+mini+mini_2 

"""
Approach 2 :
Sorted array all the element except the first element
Time complexity : O nlogn
Space complexity : On
"""
def minimumCost(nums: list[int]) :
        a = nums[0]
        sorted_nums = sorted(nums[1:])

        return a+sorted_nums[0]+sorted_nums[1]
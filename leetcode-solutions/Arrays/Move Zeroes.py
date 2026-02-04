"""Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Problem link : https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=programming-skills
"""

def moveZeroes(nums: list[int]) :
    """
    Do not return anything, modify nums in-place instead.
    """
    pointer = -1
    n = len(nums)
    for i in range(n):
        if nums[i]==0:
            pointer =i
            break
    
    if pointer == -1:
        return 
    else:
        for i in range(pointer+1,n):
            if nums[i] != 0:
                nums[i], nums[pointer] = nums[pointer],nums[i]
                pointer+=1
    
    return 
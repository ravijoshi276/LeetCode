"""Next Permutation 

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

problem link :https://leetcode.com/problems/next-permutation/
"""


def nextPermutation( nums: list[int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    def rotate(arr,index_start,index_switch):
            arr[index_start],arr[index_switch] = arr[index_switch],arr[index_start]
            arr[index_start+1:] = arr[index_start+1:][::-1]
    
    n = len(nums)-1
    end = n
    flag = 0
    while(end>=0):
        if end ==len(nums)-1:
            end-=1
            continue
        if nums[end] < nums[end+1]:
            flag =1
            end = end+1
            break
        end-=1
    if flag == 0:
        nums.reverse()
    else:
        if end == n :
            nums[end],nums[end-1] = nums[end-1],nums[end]
        else :
            if nums[end-1]<nums[n]:
                rotate(nums,end-1,n)
            elif nums[end-1] > nums[n]:
                i = n
                while(nums[end-1]>=nums[i]):
                    i-=1
                rotate(nums,end-1,i)
            else:
                i = n
                while(nums[end-1]==nums[i]):
                    i-=1
                rotate(nums,end-1,i)
"""
Logic :
"""
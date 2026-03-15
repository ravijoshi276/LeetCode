"""Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Problem Link:https://leetcode.com/problems/permutations-ii/?envType=problem-list-v2&envId=array"""


def permuteUnique( nums: list[int]) :
    res=[]
    n=len(nums)
    nums.sort()
    def generate_permutations(nums,n):
        end=n-1
        p2=n-1
        while(end>0 and nums[end-1]>=nums[end]):
            end-=1
        if end==0:
            nums= nums[:][::-1]
            return nums.copy()
        elif end==n-1:
            nums[n-1],nums[n-2]=nums[n-2],nums[n-1]
            return nums.copy()
        while(p2>end and nums[p2]<=nums[end-1]):
            p2-=1
        
        nums[p2],nums[end-1]= nums[end-1],nums[p2]
        nums[end:]=nums[end:][::-1]
        return nums.copy()

    per=1
    for i in range(1,n+1):
        per *=i
    
    for i in range(per):
        out=generate_permutations(nums,n)
        if out in res:
            continue
        res.append(out)
    return res
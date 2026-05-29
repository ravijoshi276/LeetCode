"""Minimum Element After Replacement With Digit Sum

You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.
problem Link :https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/?envType=daily-question&envId=2026-05-29
"""
def minElement(self, nums: List[int]) -> int:
        n= len(nums)
        res=1000
        for i in range(n):
            num =nums[i]
            temp=0
            while(num>0):
                temp+=num%10
                num//=10
            res= min(res,temp)
        return res

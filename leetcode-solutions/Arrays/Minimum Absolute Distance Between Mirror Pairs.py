"""Minimum Absolute Distance Between Mirror Pairs


You are given an integer array nums.

A mirror pair is a pair of indices (i, j) such that:

0 <= i < j < nums.length, and
reverse(nums[i]) == nums[j], where reverse(x) denotes the integer formed by reversing the digits of x. Leading zeros are omitted after reversing, for example reverse(120) = 21.
Return the minimum absolute distance between the indices of any mirror pair. The absolute distance between indices i and j is abs(i - j).

If no mirror pair exists, return -1.

Problem Link: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/description/?envType=daily-question&envId=2026-04-17
"""


def minMirrorPairDistance( nums: list[int]) :
        def reverseNUmber(num):
            res=0
            while(num):
                res = res *10 +num%10
                num //=10
            
            return res
        mpp={}
        n =len(nums)
        m=n
        for i in range(n-1,-1,-1):
            rev = reverseNUmber(nums[i])
            if  rev in mpp:
                m=min(m,mpp[rev]-i)
           
            mpp[nums[i]]=i
        
        return m if m!=n else -1
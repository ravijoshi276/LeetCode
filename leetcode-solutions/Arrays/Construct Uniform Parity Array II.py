"""Construct Uniform Parity Array II

You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

nums2[i] = nums1[i]​​​​​​​
nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1
Return true if it is possible to construct such an array, otherwise return false.

Problem Link: https://leetcode.com/problems/construct-uniform-parity-array-ii/"""
def uniformArray(nums1: list[int]) -> bool:
    if len(nums1)==1:
        return True
    min_ele= nums1[0]
    max_ele=nums1[0]
    cnt_odd=0
    cnt_even=0
    for i in nums1:
        if i < min_ele:
            min_ele=i
        if i > max_ele:
            max_ele=i
        if i &1 ==1:
            cnt_odd+=1
            continue
        cnt_even+=1
    ans=False
    if min_ele &1==1:
        ans=True
            
    else:
        if not cnt_odd:
            ans=True
    return ans
                
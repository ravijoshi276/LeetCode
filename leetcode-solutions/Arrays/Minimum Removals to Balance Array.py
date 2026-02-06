"""Minimum Removals to Balance Array

You are given an integer array nums and an integer k.

An array is considered balanced if the value of its maximum element is at most k times the minimum element.

You may remove any number of elements from nums​​​​​​​ without making it empty.

Return the minimum number of elements to remove so that the remaining array is balanced.

Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

 


Problem link : https://leetcode.com/problems/minimum-removals-to-balance-array/?envType=daily-question&envId=2026-02-06
"""

"""Logic:
Sliding window apporact:  
 * we move the pointer till the element nums[p2]/nums[p1]<k
 * we record the maximum lenth till now

 Note : Not using (p2-p1+1) as i am already increasing p2 before calculating maximum

"""
def minRemoval(nums: list[int], k: int) :
        nums.sort()
        n = len(nums)
        p1=0
        p2=0
        m = -1
        while(p2<=n-1):
            
            if nums[p2] / nums[p1] <=k:
                p2+=1
                m = max(m,(p2-p1)) # Not using p2-p1 +1 for length as already moving p2 before calculating maximum
               
            else:
                p1+=1
            
        
        return n-m
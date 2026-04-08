"""XOR After Range Multiplication Queries I

You are given an integer array nums of length n and a 2D integer array queries of size q, where queries[i] = [li, ri, ki, vi].

For each query, you must apply the following operations in order:

Set idx = li.
While idx <= ri:
Update: nums[idx] = (nums[idx] * vi) % (109 + 7)
Set idx += ki.
Return the bitwise XOR of all elements in nums after processing all queries.

Problem Link: https://leetcode.com/problems/xor-after-range-multiplication-queries-i/?envType=daily-question&envId=2026-04-08"""

def xorAfterQueries(nums: list[int], queries: list[List[int]]) -> int:
        m=10**9+7
        for l,r,k,v in queries:
            for i in range(l,r+1,k):
                nums[i] = nums[i]*v %m        
        xor=0
        for i in nums:
            xor^=i
        
        return xor
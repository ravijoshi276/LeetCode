"""3Sum Closest
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

problem link : https://leetcode.com/problems/3sum-closest/description/?envType=problem-list-v2&envId=array
"""

def threeSumClosest(nums: list[int], target: int):
        minimum_diff = float('inf')
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i !=0 and nums[i]== nums[i-1]:
                continue
            first = nums[i]
            j = i+1
            k = n-1
            while(j<k):
                second = nums[j] + nums[k]
                temp = minimum_diff
                three_sum = first + second
                minimum_diff = min(abs(target-three_sum),minimum_diff)
                if not temp == minimum_diff:
                    res = first+second
                if three_sum <target:
                    j+=1
                elif three_sum > target:
                    k-=1
                else:
                    return three_sum
        return res
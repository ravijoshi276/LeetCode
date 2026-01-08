"""128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Problem Link : https://leetcode.com/problems/longest-consecutive-sequence/description/

"""
def longestConsecutive(nums) :
        d = set(nums) # convert nums to a set data structure
        best = 0
        for key in d:
            if key -1 not in d: # for a starting point
                
                y = key +1
                while y in d: # search till last number in set
                    y+=1
                best = max(y-key,best) # return the maximum


        return best

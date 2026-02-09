"""Transformed Array

Hint
You are given an integer array nums that represents a circular array. Your task is to create a new array result of the same size, following these rules:

For each index i (where 0 <= i < nums.length), perform the following independent actions:
If nums[i] > 0: Start at index i and move nums[i] steps to the right in the circular array. Set result[i] to the value of the index where you land.
If nums[i] < 0: Start at index i and move abs(nums[i]) steps to the left in the circular array. Set result[i] to the value of the index where you land.
If nums[i] == 0: Set result[i] to nums[i].
Return the new array result.

Note: Since nums is circular, moving past the last element wraps around to the beginning, and moving before the first element wraps back to the end.

problem link : https://leetcode.com/problems/transformed-array/description/?envType=daily-question&envId=2026-02-05
"""

#Solution 
"""
Logic : 
* Case when nums[i] is positive.
    *  Just add it to index and use then sum % length to find the position to go to the right. This gives to total number of steps to go to the right.
* Case when nums[i] is 0.
    * just append the nums[i]
* Case when nums[i] is negative.
    * modulo of that number with length on array we get required ansewer then use:(index + nums[i]%length)%length to find required answer. example(-11 % 5 = +4, -7 % 5 = +3)
    * We can convert nums[i] in positive and use (index + length - (abs(nums[i]%length)))%length to find required index
"""
def constructTransformedArray(nums: list[int]):
    res =[]
    n = len(nums)
    for i in range(n):
        
        if nums[i]>0:
            p = (nums[i] + i)%n
            res.append(nums[p])
        elif nums[i] ==0:
            res.append(nums[i])
        else:
            p = (i + (nums[i]%n))%n #taking directly modulo of negative number. We can use other formula mentioned above
            res.append(nums[p])
    return res

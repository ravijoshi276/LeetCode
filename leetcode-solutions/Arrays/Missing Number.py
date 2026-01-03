"""Missing Number
Given an array nums containing n distinct numbers in the 
range [0, n], return the only number in the range that is
missing from the array.

problem link : https://leetcode.com/problems/missing-number/description/


Input: nums = [3,0,1]

Output: 2
 """


def missingNumber(nums) :
    #Solution below
    xor1 = 0
    xor2 = 0
    """XOR of same bit will result in zero and 0 xor number is the same number"""
    for i in range(len(nums)):
        xor1 ^= i
        xor2 ^= nums[i]

    return xor1^xor2 ^len(nums) 
nums = [3,0,1]

res = missingNumber(nums)
print(res)
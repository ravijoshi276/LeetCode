"""Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Problem Link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=problem-list-v2&envId=array"""

def twoSum( numbers: List[int], target: int) -> List[int]:
        mpp ={}
        index =1
        for i in numbers:
            look_up = target-i
            if not look_up in mpp:
                mpp[i]= index
            else:
                return [mpp[look_up],index]
            index+=1
        
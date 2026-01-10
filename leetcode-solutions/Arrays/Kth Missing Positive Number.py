"""1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

Problem link : https://leetcode.com/problems/kth-missing-positive-number/description/

Input: arr = [2,3,4,7,11], k = 5
Output: 9
"""


def findKthPositive(arr, k: int):
        l, r = 0, len(arr) # Selecting a start and end
        while l < r: #Find an index at which there are more than k mising element on left
            m = (l + r) // 2
            if arr[m] - 1 - m < k:
                l = m + 1
            else:
                r = m
        return l + k #Returning k + index found

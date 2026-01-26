"""Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

problem link : https://leetcode.com/problems/minimum-absolute-difference/description/?envType=daily-question&envId=2026-01-26
"""

def minimumAbsDifference(arr):
    arr.sort()
    n = len(arr)-1
    m_diff = float('inf')
    for i in range(n):
        diff = abs(arr[i+1]-arr[i])
        if diff < m_diff:
            m_diff = diff
    res = []
    for i in range(n):
        diff = abs(arr[i]-arr[i+1])
        if diff <= m_diff:
            res.append([arr[i],arr[i+1]])

    return res



"""Minimum Capacity Box

You are given an integer array capacity, where capacity[i] represents the capacity of the ith box, and an integer itemSize representing the size of an item.

The ith box can store the item if capacity[i] >= itemSize.

Return an integer denoting the index of the box with the minimum capacity that can store the item. If multiple such boxes exist, return the smallest index.

If no box can store the item, return -1.

Problem Link: https://leetcode.com/problems/minimum-capacity-box/description/"""


def minimumIndex( capacity: list[int], itemSize: int) :
        index=-1
        diff=float('inf')
        for i in range(len(capacity)):
            if capacity[i]==itemSize:
                return i
            elif capacity[i]>itemSize:
                if diff > capacity[i]-itemSize:
                    diff = capacity[i]-itemSize
                    index =i
            
        return index
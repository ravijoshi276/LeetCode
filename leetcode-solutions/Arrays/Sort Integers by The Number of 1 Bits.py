"""Sort Integers by The Number of 1 Bits

You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
Problem Link : https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/?envType=daily-question&envId=2026-02-25"""

def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key= lambda x : (bin(x).count('1'),x))
        return arr
"""74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Problem Link :https://leetcode.com/problems/search-a-2d-matrix/
"""

def searchMatrix( matrix, target: int):
    #Row length
    m = len(matrix)
    #Column length
    n = len(matrix[0])

    #Searching in rows and col 1
    row=0
    end = m-1
    col=0
    while (row<=end):
        mid = (row+end)//2
        if matrix[mid][col]==target:
            return True
        elif matrix[mid][col]> target:
            end = mid-1
        else:
            row = mid+1
    #Searching in col and row which is equal to end
    row = end
    end = n-1
    
    while (col<=end):
        mid = (col+end)//2
        if matrix[row][mid]==target:
            return True
        elif matrix[row][mid]> target:
            end = mid-1
        else:
            col = mid+1
    return False

    

    
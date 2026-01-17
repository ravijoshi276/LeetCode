"""240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Problem Link : https://leetcode.com/problems/search-a-2d-matrix-ii/description/
"""


def searchMatrix(matrix, target) :

    srs=0
    sre=len(matrix)-1 #Search row End
    scs = 0
    sce = len(matrix[0])-1 #Search column end
    while(0<=srs<=sre and 0 <=scs<=sce): #While then pointer srs and scs stays inside boundary
        start = srs
        end = sre
        col = scs
        #Search the index in row
        while(start<=end):
            mid = (start+end)//2
            if matrix[mid][col] == target:
                return True
            elif matrix[mid][col]< target:
                start = mid + 1
            else:
                end = mid-1
        #Update the value of start of search column
        srs = end
        if not  0<=srs<=sre:
            break
        #Search the index in column
        start = scs
        end = sce
        row = srs

        while(start<=end):
            mid = (start+end)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid +1
            else:
                end = mid-1
            
        #Update the value of start of search row
        scs = start
        
    return False
"""
Logic : 

We will search for just smaller element in row.
Then we will find the just larger element in column.
This will eleminate all the elements on the left. of both row and column and then we will repeat the same.

"""
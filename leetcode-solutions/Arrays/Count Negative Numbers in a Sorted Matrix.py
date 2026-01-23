"""Count Negative Numbers in a Sorted Matrix
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,

 return the number of negative numbers in grid.

 grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
 Output: 8

 Problem Link : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
 """


#Brute force method
"""
Going through each element and then counting all negative elements
"""
def countNegatives(grid: list[list[int]]) -> int:
    rows= len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]<0:
                count+=1
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(countNegatives(grid))
    
grid = [[3,2],[1,0]]
print(countNegatives(grid))

def countNegatives(grid: list[list[int]]) -> int:
    rows= len(grid)
    cols = len(grid[0])
    count=0
    for i in range(rows):
        start =0
        end = cols-1
        while(start<=end):
            index = (start+end)//2
            if grid[i][index] >=0:
                start = index+1
            elif grid[i][index]<0:
                end= index-1
        count += cols-start 
    
        """cols is len of col """
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(countNegatives(grid))
    
grid = [[3,2],[1,0]]
print(countNegatives(grid))

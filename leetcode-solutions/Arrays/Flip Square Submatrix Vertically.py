"""Flip Square Submatrix Vertically

You are given an m x n integer matrix grid, and three integers x, y, and k.

The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k represents the size (side length) of the square submatrix.

Your task is to flip the submatrix by reversing the order of its rows vertically.

Return the updated matrix.

 
 Problem Link : https://leetcode.com/problems/flip-square-submatrix-vertically/description/?envType=daily-question&envId=2026-03-21"""

def reverseSubmatrix(grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        start_row,start_col,end_row,end_col=x,y,x+k-1,y+k-1
        while(start_row<end_row):
            p=start_col
            while(p<=end_col):
                grid[start_row][p],grid[end_row][p]=grid[end_row][p],grid[start_row][p]
                p+=1
            start_row+=1
            end_row-=1
        return grid
"""Count Submatrices With Equal Frequency of X and Y

Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
Problem Link : https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/?envType=daily-question&envId=2026-03-19"""

def numberOfSubmatrices(grid: list[list[str]]) -> int:
        rows=len(grid)
        cols= len(grid[0])
        count=0
        x=[0]*cols
        y=[0]*cols
        for i in range(rows):
            row_x=0
            row_y=0
            for j in range(cols):
               row_x+=(grid[i][j]=='X')
               row_y+=(grid[i][j]=='Y')
               x[j]+=row_x
               y[j]+=row_y
               count+=(x[j]>0)&(x[j]==y[j]) 

        return count
"""Count Submatrices with Top-Left Element and Sum Less Than k


You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, and have a sum less than or equal to k.Problem Link :https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/submissions/1951680262/?envType=daily-question&envId=2026-03-18"""

def countSubmatrices( grid: list[list[int]], k: int):
        rows= len(grid)
        cols= len(grid[0])
        count=0
        temp=grid
        for i in range(rows):
            ff_sum=0
            for j in range(cols):
                if i==0 and j!=0:
                    ff_sum = temp[i][j] + temp[i][j-1]
                    temp[i][j]=ff_sum
                elif i>0 and j==0:
                    ff_sum = temp[i-1][j]+temp[i][j]
                    temp[i][j]=ff_sum
                elif i >0 and j >0:
                    ff_sum=temp[i][j] +temp[i-1][j] + temp[i][j-1] - temp[i-1][j-1]
                    temp[i][j]=ff_sum
                else:
                    ff_sum=temp[0][0]
                if ff_sum <=k:
                    count+=1
        return count


#Faster Solution 

def countSubmatrices(grid: list[list[int]], k: int) -> int:
        rows= len(grid)
        cols= len(grid[0])
        for row in range(rows):
            s=0
            for col in range(cols):
               s+=grid[row][col]
               grid[row][col]=s
        for col in range(cols):
            s=0
            for row in range(rows):
               s+=grid[row][col]
               grid[row][col]=s

        
        return sum(val<=k for row in grid for val in row)
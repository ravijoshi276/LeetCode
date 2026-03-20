"""Minimum Absolute Difference in Sliding Submatrix

You are given an m x n integer matrix grid and an integer k.

For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.

Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.

Note: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.

Problem Link:https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/?envType=daily-question&envId=2026-03-20
"""

#Logic
"""Append all the submatrix and then perform bruteforce on it"""

def minAbsDiff(grid: list[list[int]], k: int) :
        rows=len(grid)
        cols= len(grid[0])
        n=rows
        m=cols
        if m==n and m==k:
            m,n=1,1
        else:
            m=m-k+1
            n=n-k+1
        output=[]
        if k==1:
            return [[0]*m]*n
        for i in range(n):
            row=[]
            for j in range(m):
                sub_mat_ele=[]
                for x in range(i,i+k):
                    for y in range(j,j+k):
                        sub_mat_ele.append(grid[x][y])
                sub_mat_ele.sort(reverse=True)
                diff_min= float('inf')
                for ele in range(len(sub_mat_ele)-1):
                    diff = sub_mat_ele[ele]-sub_mat_ele[ele+1] 
                    diff_min = min(diff_min,diff) if sub_mat_ele[ele]-sub_mat_ele[ele+1]>0 else diff_min
                if diff_min ==float('inf'):
                    diff_min=0  
                row.append(diff_min)
                
            output.append(row)
    

        return output
"""Equal Sum Grid Partition I


You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

Problem Link : https://leetcode.com/problems/equal-sum-grid-partition-i/?envType=daily-question&envId=2026-03-25"""

def canPartitionGrid( grid: list[list[int]]) -> bool:
        rows = len(grid)
        cols= len(grid[0])
        row_s=[]
        col_s=[]
        for i in range(rows):
            if i > 0:
                row_s.append(row_s[i-1]+ sum(grid[i]))
            else:
                row_s.append(sum(grid[i]))
        transposed= zip(*grid)
        p=0
        for i in transposed:
            if p >0:
                col_s.append(col_s[p-1]+sum(i))
            else:
                col_s.append(sum(i))
            p+=1
        total= max(row_s[-1],col_s[-1])
        for i in row_s:
            if i *2 == total:
                return True
            elif i * 2 > total:
                break
        for i in col_s:
            if i *2 == total:
                return True
            elif i * 2 > total:
                break
        return False
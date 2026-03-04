"""Special Positions in a Binary Matrix

Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 
Problem Link : https://leetcode.com/problems/special-positions-in-a-binary-matrix/?envType=daily-question&envId=2026-03-04"""


def numSpecial( mat: List[List[int]]) -> int:
        rows = len(mat)
        cols= len(mat[0])
        mpp_row ={}
        mpp_col={}
        ones= set()
        count=0
        
        for i in range(rows):
            for j in range(cols):
                num = mat[i][j]
                if num ==1:
                    mpp_row[i] = mpp_row.get(i,0)+1
                    mpp_col[j] = mpp_col.get(j,0)+1
                    ones.add((i,j))
        for i in ones:
            if mpp_row[i[0]] ==1 and mpp_col[i[1]]==1:
                count+=1
                
        return count
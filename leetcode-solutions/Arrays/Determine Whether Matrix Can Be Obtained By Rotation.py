"""Determine Whether Matrix Can Be Obtained By Rotation

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
Problem Link: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/?envType=daily-question&envId=2026-03-22"""

def findRotation(mat: list[list[int]], target: list[list[int]]) -> bool:
        rows=len(mat)
        cols = len(mat[0])
        def rotate():
            for i in range(rows):
                for j in range(i,cols):
                    mat[i][j],mat[j][i]= mat[j][i],mat[i][j]
            for i in range(rows):
                mat[i][:]= mat[i][:][::-1]
        if mat == target:
            return True
        rotate()
        if mat == target:
            return True
        rotate()
        if mat == target:
            return True
        rotate()
        if mat == target:
            return True
        return False

"""Matrix Similarity After Cyclic Shifts

You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.

The following proccess happens k times:
Problem Link :https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/?envType=daily-question&envId=2026-03-27"""

def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        rows=len(mat)
        k = k%len(mat[0])
        temp = copy.deepcopy(mat)
        for i in range(rows):
            temp[i][:k]= temp[i][:k][::-1]
            temp[i][k:]= temp[i][k:][::-1]
            temp[i]= temp[i][:][::-1]
            if mat[i] != temp[i]:
                return False
       
        return True
    
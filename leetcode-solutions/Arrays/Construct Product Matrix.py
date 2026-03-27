"""Construct Product Matrix

Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if the following condition is met:

Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j]. This product is then taken modulo 12345.
Return the product matrix of grid.

Problem Link: https://leetcode.com/problems/construct-product-matrix/?envType=daily-question&envId=2026-03-24"""

def constructProductMatrix(grid: list[list[int]]) :
        rows= len(grid)
        cols=len(grid[0])
        pre = [[0]*cols for _ in range(rows)]
        p_sum=1
        MOD=12345
        for i in range(rows):
            for j in range(cols):
                pre[i][j]=  p_sum 
                p_sum = grid[i][j] * p_sum % MOD
        suff=1
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                pre[i][j] = pre[i][j] *  suff % MOD
                suff =  grid[i][j] * suff % MOD
        
        return pre
        
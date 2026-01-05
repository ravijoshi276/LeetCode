"""1975. Maximum Matrix Sum
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Link : https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2026-01-05
"""

def maxMatrixSum(matrix: list[list[int]]):
        total = 0 # Adds the total
        neg_count =0 # Count of negative
        minAbs = float('inf') #Store the minimum absolute
        for row in matrix:
            for value in row:
                if value < 0:
                    neg_count+=1
                val = abs(value) # absolute value of number
                total+=val
                minAbs = min (minAbs, val)
        
        if neg_count %2 ==0: # Check if neg_count is even
            return total
        return total - 2 * minAbs # Return if negative count is odd

"""
Logic :

1. We go through each number and add all there absolute value and also store the count of negative.
2. We store the nummber with least absolute value.
3. We check if count of negative number is odd or even.
Note : if there are even number of negative value we can convert all of them 
4 . If even count of negative value we return total
5. If the count is odd, we will fail to convert just one value that will be minumum.
6 We will subtract 2 * minAbs value as we added it before in total 

"""
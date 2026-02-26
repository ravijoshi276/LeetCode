"""Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

Problem Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2026-02-26"""

 def numSteps(s: str) :
        num = int(s,2)
        print(len(s))
        count=0
        while(num>1):
            
            if num %2 ==0:
                count+=1
                num=num//2
            else:
                count+=1
                num += 1
                
        return count
"""Prime Number of Set Bits in Binary Representation

Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.
 
Problem Link :https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/?envType=daily-question&envId=2026-02-21
"""
def countPrimeSetBits(left: int, right: int) -> int:
        def isPrime(n): #Checks if the number is prime
            if n==1:
                return False
            elif n <4:
                return True
            x = n **(1/2)
            x = int(x) +1
            for i in range(2,x):
                if n %i ==0:
                    return False
            
            return True
        def toBinary_string(n): #converts the number to binary string
            res = bin(n)[2:]
            return res
        cnt = 0
        for i in range(left,right+1):
            s = toBinary_string(i)
            n = s.count('1') #Count the number is 1's
            if isPrime(n):
                cnt+=1
        
        return cnt
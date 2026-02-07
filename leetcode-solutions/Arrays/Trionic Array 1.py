"""Trionic Array I

You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.
"""
#Brute force solution
"""
Logic : Defined a tronic array with required solution

Match if the given array follows the same logic.
Explaination :
I have declared a tronic array asc with [True, False, True]

* There can be 2 cases either its ascending and or its descending and it should match the tronic array.
* Case when it does not match we move the pointer to the next (Means that the array is now following descending order)
"""
def isTrionic(nums: list[int]) :
        asc =[True,False,True] #Tonic Array
        p=0
        n = len(nums)
        if nums[0]> nums[1]:
            return False
        for i in range(n-1):
            if nums[i] < nums[i+1] and asc[p] :
                continue

            elif nums[i] > nums[i+1] and not asc[p]:
                
                continue
            elif nums[i]== nums[i+1]:
                return False
            
            else:
                    p+=1
                 
            
            if p > 2:
                return False
            
        if p < 2:
            return False
       

        return True

#Better Solution
"""
Logic: we flip sign every time there is change in order and count the switches
"""
def isTrionic(nums):
    n = len(nums)
    #Edge case where
    if nums[0]> nums[1]:
        return False
    sign =1
    switches = 0
    for i in range(n-1):
        diff = nums[i+1] - nums[i]
        if diff == 0: #Case where both number are same
            return False
        elif diff * sign < 0:
            sign *= -1
            switches +=1
    if switches != 2:
         return False
    
    return True

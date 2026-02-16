"""Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Problem Link : https://leetcode.com/problems/max-consecutive-ones-iii/description/
"""
"""
Logic: Sliding window and approach

"""
def longestOnes(nums: list[int], k: int) :
        zeros= 0
        n = len(nums)
        p1=0 # A start pointer
        p2=0 # A end pointer
        m = -1 #Storing maximum
        while(p2<n):
            if k == 0:
                while(p1<n and nums[p1]==0):
                    p1+=1
                if p1<n:
                    p2 = p1+1
                else:
                    p2=p1
                while(p2<n and nums[p2]==1):
                    p2+=1
                m = max(m,p2-p1)
                p1=p2
            else:


                while(p2<n and (zeros<k or nums[p2]==1)):
                    
                    if nums[p2]==0:
                        zeros+=1
                    p2+=1
                    
            
                m = max(m,p2-p1)
                while(p1<p2 and zeros>=k ):
                
                    if nums[p1]== 0:
                        zeros-=1
                        
                    p1+=1
                if p2==p1:
                    p2+=1
        return m


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums,k))

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(longestOnes(nums,k))
nums =[1,1,1,0,0,0,1,1,1,1,0]
k=2
print(longestOnes(nums,k))
nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k=3
print(longestOnes(nums,k))
nums=[0,0,0,1]
k=4
print(longestOnes(nums,k))
nums=[0,0,1,1]
k=1
print(longestOnes(nums,k))

nums=[0,0,1,1,1,0,0] 
k=0
print(longestOnes(nums,k)) 
nums=[0,0,0,0]
k=0
print(longestOnes(nums,k))

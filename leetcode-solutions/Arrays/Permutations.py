"""Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Problem Link :https://leetcode.com/problems/permutations/description/?envType=problem-list-v2&envId=array"""

def permute(nums: list[int]) :
        res =[]
        n = len(nums)
        if n==1:
            res.append(nums)
            return res
        
        permutations = 1
        for i in range(1,n+1):
            permutations *=i
        res.append(nums)
        nums2 = nums.copy()
        for i in range(1,permutations):
            nums2= nums2.copy()
            end = n-1
            while(True):
                if nums2[end]>nums2[end-1]:
                    break
                end-=1
            if end ==0:
                nums2[:] = nums2[:][::-1]
            elif end == n-1:
                nums2[end],nums2[end-1]= nums2[end-1],nums2[end]
            else:
                pointer = n-1
                while(nums2[pointer]<nums2[end-1]):
                    pointer-=1
                nums2[pointer],nums2[end-1] = nums2[end-1],nums2[pointer]
                nums2[end:]=nums2[end:][::-1]

            res.append(nums2)

        return res 
        
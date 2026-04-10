"""Minimum Distance Between Three Equal Elements I
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.Minimum Distance Between Three Equal Elements I

You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.
Problem Link : https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/?envType=daily-question&envId=2026-04-10"""

def minimumDistance(self, nums: list[int]) -> int:
        res =-1
        mpp = defaultdict(list)
        out=[]
        for i in range(len(nums)):
            t = nums[i]
            if t in mpp:
                mpp[t][0]+=1
                mpp[t].append(i)
                if mpp[t][0]==3:
                    out.append(t)
            else:
                mpp[t].append(1)
                mpp[t].append(i)
        if len(out):
            res=300
            for i in out:
                for j in range(1,len(mpp[i])-2):
                    diff = 2*(mpp[i][j+2]-mpp[i][j])
                    res = min(res,diff)
                
                if res ==4:
                    return res
        
        return res
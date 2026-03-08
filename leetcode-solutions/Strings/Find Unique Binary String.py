"""Find Unique Binary String

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
Problem Link :https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2026-03-08"""

def findDifferentBinaryString(nums: List[str]) -> str:
        n = len(nums[0])
        res = ["0"] *n
        nums.sort()
        for i,x in enumerate(nums):
            if x[i]=="0":
                res[i]='1'
            
        return "".join(res)
        
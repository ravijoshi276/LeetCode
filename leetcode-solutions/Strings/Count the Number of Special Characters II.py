"""Count the Number of Special Characters II

You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

Problem Link : https://leetcode.com/problems/count-the-number-of-special-characters-ii/?envType=daily-question&envId=2026-05-27
"""

def numberOfSpecialChars(self, word: str) -> int:
        mpp ={}
        c=0
        n= len(word)
        for i in range(n):
            val = ord(word[i])
            if val <= 90 and (val+32) in mpp and (mpp.get(val+32)>0):
                c+=1
                mpp[val+32] = 0
            elif val < 90 and val+32 not in mpp:
                mpp[val+32]=-1
            elif val > 90 and val in mpp and mpp[val]==0:
                print("here",val)
                mpp[val]=-1
                c-=1
            elif val > 90 and val not in mpp:
                mpp[val]=1
            elif mpp.get(val,False)>0:
                continue
            
        
        return c
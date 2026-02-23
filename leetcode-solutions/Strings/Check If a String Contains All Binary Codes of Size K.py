"""Check If a String Contains All Binary Codes of Size K

Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.
Problem Link : https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23 """


# Logic
"""
1. Check for length: if a substring should have all the code it must be alteast 2**k long.
    Exmaple : for k = 2, n>=4 i.e "0110"
2. When Adding chuncks of substing to the set it should be equal to number of codes.
"""
def hasAllCodes(s: str, k: int) -> bool:
        n = len(s)
        num_code = 2**k
        if n >= num_code:
            set_codes = set()
            for i in range(0,n+1-k):
                set_codes.add(s[i:i+k])
            if len(set_codes)== num_code:
                return True
        return False
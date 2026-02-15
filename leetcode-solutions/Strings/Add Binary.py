"""Add Binary

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Problem Link :https://leetcode.com/problems/add-binary/submissions/1919560645/?envType=daily-question&envId=2026-02-15"""


def addBinary(self, a: str, b: str) -> str:
    a_binary = int(a,2)
    b_binary = int(b,2)
    print(a_binary,b_binary)
    return str(bin(a_binary+b_binary))[2:]
        
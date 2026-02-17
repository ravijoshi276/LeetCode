"""Reverse Bits

Reverse bits of a given 32 bits signed integer.

Problem Link :https://leetcode.com/problems/reverse-bits/description/?envType=daily-question&envId=2026-02-17
"""


def reverseBits( n: int) -> int:
        n_bit = bin(n)
        n_bit_reversed = str(n_bit)[::-1]
        n_bit_reversed = n_bit_reversed[:-2]
        n_bit_reversed = n_bit_reversed + (32-len(n_bit_reversed)) *"0"
        
        
        return int(n_bit_reversed,2)
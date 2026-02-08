"""String to Integer (atoi)


The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

Probleem :ink :https://leetcode.com/problems/string-to-integer-atoi/description/
"""



def myAtoi(s: str):
    int_min = -2 ** 31
    int_max = 2 **31 -1
    
    def helper(string,index,sign,num=0):
        """This function is recursive and calls itself till the index of string is at a digit.
        The function takes string with a starting index at a digit and sign. and num that will be used to create the required number"""
        if index >= len(s) or not string[index].isdigit():
            
            return sign * num

        num = num *10 +int(s[index])
        
        if sign * num <= int_min: return int_min
        if sign * num >= int_max: return int_max

        return helper(string,index+1,sign,num)
    
    i =0
    n = len(s)
    if n ==0:
        return 0
    while i<n and s[i]==" ":
        i+=1
    sign=1
    if i < n:
        sign = -1 if s[i]=="-" else 1
    else:
        return 0
    if (s[i]=="-" or s[i]=="+") and i < n-1:
        i+=1
    
    return helper(s,i,sign,0)

        
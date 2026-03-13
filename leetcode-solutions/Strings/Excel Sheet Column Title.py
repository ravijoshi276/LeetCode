"""Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

Problem Link : https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string"""

 def convertToTitle( columnNumber: int) -> str:
        number = columnNumber
        res =""
        base= 1
    
        while(number>0):
            if number%26 != 0:
                res= chr(64+number%26)+res
            else:
                res= chr(64+26)+res
                number = number//26 - 1
                continue
            number = number //26
        return res

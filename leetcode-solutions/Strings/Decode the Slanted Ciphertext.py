"""Decode the Slanted Ciphertext

A string originalText is encoded using a slanted transposition cipher to a string encodedText with the help of a matrix having a fixed number of rows rows.

originalText is placed first in a top-left to bottom-right manner.


The blue cells are filled first, followed by the red cells, then the yellow cells, and so on, until we reach the end of originalText. The arrow indicates the order in which the cells are filled. All empty cells are filled with ' '. The number of columns is chosen such that the rightmost column will not be empty after filling in originalText.

encodedText is then formed by appending all characters of the matrix in a row-wise fashion.


The characters in the blue cells are appended first to encodedText, then the red cells, and so on, and finally the yellow cells. The arrow indicates the order in which the cells are accessed.

For example, if originalText = "cipher" and rows = 3, then we encode it in the following manner:


The blue arrows depict how originalText is placed in the matrix, and the red arrows denote the order in which encodedText is formed. In the above example, encodedText = "ch ie pr".

Given the encoded string encodedText and number of rows rows, return the original string originalText.

Note: originalText does not have any trailing spaces ' '. The test cases are generated such that there is only one possible originalText.

Problem Link : https://leetcode.com/problems/decode-the-slanted-ciphertext/?envType=daily-question&envId=2026-04-04"""

#Brutte Force Solution
def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        l=len(encodedText)
        cols= l//rows
        enCodedmat=[]
        p = 0
        for i in range(rows):
            row=[]
            for j in range(cols):
                row.append(encodedText[p])
                p+=1 
            enCodedmat.append(row)
        res=""
        for j in range(cols):
            p=j
            for i in range(rows):
                res+=enCodedmat[i][p]
                p+=1
                if p==cols:
                    break

        return res.rstrip()

#Optimal solution
def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        l=len(encodedText)
        if rows==1 or l<=rows:
            return encodedText.rstrip()
        cols= l//rows
        org_text=[]
        res=""
        p=0
        for j in range(cols): #Adding all the element in diagonal index
            p=j
            for i in range(rows):
                org_text.append(encodedText[p])
                p+=(cols+1)
                if p>=l:
                    break
        return "".join(org_text[:]).rstrip()
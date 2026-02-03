"""Integer to Roman
12. Integer to Roman
Medium
Topics
premium lock icon
Companies
Seven different symbols represent Roman numerals with the following values:


Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

Problem link :https://leetcode.com/problems/integer-to-roman/description/"""

def bs(lst,target): #Binary search
                start =0
                end =len(lst)-1
                while(start<=end):
                        mid =(start+end)//2
                        if lst[mid] < target:
                                start = mid+1
                        elif lst[mid] > target:
                                end = mid-1
                        else:
                                return lst[mid]
                return lst[start]
def intToRoman( num: int):
        
        l = [1,5,10,50,100,500,1000]
        d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res =""
        p =1 
        a = num
        
        while(a>0):
                digit = a % (p *10) #Extract place digit
                x = int(digit/p)
                if x == 4 or x ==9:
                    #Round to and write in that form
                    val = bs(l,digit)
                    res = d[val] + res
                   
                    res = d[val-digit] + res
                elif x > 5:
                        val = bs(l,5*p)
                        res = (x-5) * d[p] + res
                        res = res = d[val] + res
                        
                else:
                        res = d.get(digit,x * d[p]) + res
                a -= (x*p)
                p = p *10
               
        
        return res


n = [3999,199,1249,1500,999,249,49]
for i in n:
    
    print(intToRoman(i),":",i)


       
        
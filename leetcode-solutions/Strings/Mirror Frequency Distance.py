"""Mirror Frequency Distance

You are given a string s consisting of lowercase English letters and digits.

For each character, its mirror character is defined by reversing the order of its character set:

For letters, the mirror of a character is the letter at the same position from the end of the alphabet.
For example, the mirror of 'a' is 'z', and the mirror of 'b' is 'y', and so on.
For digits, the mirror of a character is the digit at the same position from the end of the range '0' to '9'.
For example, the mirror of '0' is '9', and the mirror of '1' is '8', and so on.
For each unique character c in the string:

Let m be its mirror character.
Let freq(x) denote the number of times character x appears in the string.
Compute the absolute difference between their frequencies, defined as: |freq(c) - freq(m)|
The mirror pairs (c, m) and (m, c) are the same and must be counted only once.

Return an integer denoting the total sum of these values over all such distinct mirror pairs.©leetcode

Problem Link : https://leetcode.com/contest/weekly-contest-496/problems/mirror-frequency-distance/"""

def mirrorFrequency(self, s: str) -> int:
        mpp={}
        cnt=0
        for i in s:
            if i.isdigit():
                num = int(i)
                if (9-num) in mpp:
                    cnt-=1
                    mpp[9-num]=mpp[9-num]-1
                    if mpp[9-num]==0:
                        mpp.pop(9-num)
                else:
                    cnt+=1
                    mpp[num]= mpp.get(num,0)+1
            else:
                if i <='m':
                    if(122-(ord(i)-97)) in mpp:
                        cnt-=1
                        mpp[122-(ord(i)-97)] = mpp[122-(ord(i)-97)]-1
                        if mpp[122-(ord(i)-97)]==0:
                            mpp.pop(122-(ord(i)-97))
                    else:
                        cnt+=1
                        mpp[ord(i)]= mpp.get(ord(i),0)+1
                else:
                    if (97+122-ord(i)) in mpp:
                        cnt-=1
                        mpp[97+122-ord(i)] -=1
                        if mpp[97+122-ord(i)]==0:
                            mpp.pop(97+122-ord(i))
    
                    else:
                        cnt+=1
                        mpp[ord(i)]= mpp.get(ord(i),0)+1
                
        return cnt©leetcode
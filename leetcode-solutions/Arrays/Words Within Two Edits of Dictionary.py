"""Words Within Two Edits of Dictionary

You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.
Problem link:https://leetcode.com/problems/words-within-two-edits-of-dictionary/?envType=daily-question&envId=2026-04-22"""

def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        res =[]
        for i in range(len(queries)):
            w1 = queries[i]
            for k in range(len(dictionary)):
                w2= dictionary[k]
                if w2==w1:
                    res.append(w1)
                    break
                else:
                    cnt=0
                    for j in range(len(w1)):
                        if w1[j] != w2[j]:
                            cnt+=1
                        if cnt>2:break
                    if cnt<=2:
                        res.append(w1)
                        break
                
        return res
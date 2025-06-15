class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1 = i2 = 0
        res = ""

        while i1 < len(word1) or i2 < len(word2):
            res += word1[i1] if i1 < len(word1) else ""
            res += word2[i2] if i2 < len(word2) else ""

            i1 += 1
            i2 += 1
        
        return res
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i]
            res += word2[i]

        i += 1
        if i < len(word1):
            return res + word1[i:]
        elif i < len(word2):
            return res + word2[i:]
        else:
            return res
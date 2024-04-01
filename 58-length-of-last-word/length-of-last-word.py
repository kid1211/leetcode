class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = 0
        res = 0
        for l in s+" ":
            if l == " ":
                res = word if word else res
                word = 0
            else:
                word += 1
        return res
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dup = set()
        res = 0

        for l in s:
            if l in dup:
                dup.remove(l)
                res += 2
            else:
                dup.add(l)
        
        if dup:
            res += 1
        return res
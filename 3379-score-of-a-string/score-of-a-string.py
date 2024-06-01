class Solution:
    def scoreOfString(self, s: str) -> int:
        last = s[0]
        res = 0
        for i in range(1, len(s)):
            res += abs(ord(last) - ord(s[i]))
            last = s[i]
        
        return res
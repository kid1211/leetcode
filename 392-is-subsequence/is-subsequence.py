class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        for right in range(len(s)):
            while left < len(t) and t[left] != s[right]:
                left += 1
            
            if left < len(t):
                left += 1
            else:
                return False

        return True

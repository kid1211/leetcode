class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()

        res = right = 0
        for left in range(len(s)):
            while right < len(s) and s[right] not in unique:
                unique.add(s[right])
                right += 1
    
            if left < right:
                res = max(res, right - left)
            
            unique.remove(s[left])
        return res
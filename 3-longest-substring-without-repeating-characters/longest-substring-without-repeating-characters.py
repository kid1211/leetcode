class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        n = len(s)
        res = right = 0
        for left in range(n):
            while right < n and s[right] not in unique:
                unique.add(s[right])
                right += 1

            res = max(res, len(unique))
            unique.remove(s[left])
        return res

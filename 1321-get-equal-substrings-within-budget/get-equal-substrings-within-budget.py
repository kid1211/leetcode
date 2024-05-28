class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = left = curr = 0

        for right in range(len(s)):
            curr += abs(ord(s[right]) - ord(t[right])) 

            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            res = max(res, right - left + 1)
        return res
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = res = 0
        unique = defaultdict(int)
        for right in range(len(s)):
            unique[s[right]] += 1

            while left < right and len(unique) > k:
                unique[s[left]] -= 1
                if unique[s[left]] == 0:
                    del unique[s[left]]
                left += 1

            if len(unique) <= k:
                res = max(res, right - left + 1)
        return res
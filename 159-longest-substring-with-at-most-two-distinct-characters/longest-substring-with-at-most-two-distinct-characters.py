class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = res = 0
        unique = defaultdict(int)
        for right in range(len(s)):
            unique[s[right]] += 1

            while left < right and len(unique) > 2:
                unique[s[left]] -= 1
                if unique[s[left]] == 0:
                    del unique[s[left]]
                left += 1
            res = max(res, right - left + 1)
        return res
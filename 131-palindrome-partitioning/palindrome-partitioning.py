class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s == s[::-1]

        @cache
        def dfs(s):
            if len(s) == 1:
                return [[s]]

            res = []
            for i in range(1, len(s)):
                if not isPalindrome(s[:i]):
                    continue
                for ans in dfs(s[i:]):
                    res += [
                        [s[:i]] + ans
                    ]
            if isPalindrome(s):
                res += [[s]]
            return res
        return dfs(s)
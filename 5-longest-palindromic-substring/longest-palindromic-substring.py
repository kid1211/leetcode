class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'
        
        def expandMid(idx):
            step = 0
            while (
                idx + step < len(s) and
                idx - step >= 0 and
                s[idx + step] == s[idx - step]
            ):
                step += 1
            return step - 1

        res = (0, 0) # mid, step

        for i in range(len(s)):
            step = expandMid(i)

            if step > res[1]:
                res = (i, step)

        mid, step = res
        return s[mid - step: mid + step + 1].replace('#', '')

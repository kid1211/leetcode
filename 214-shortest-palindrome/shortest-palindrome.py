class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def getVal(l):
            # assume only small case
            return ord(l) - ord('a')

        hash1 = hash2 = 0
        coef = 1 # check
        longest = 0
        prime = 31
        mod = sys.maxsize // prime

        for i in range(len(s)):
            val = getVal(s[i])
            hash1 = (hash1 * prime + val) % mod
            hash2 = (hash2 + coef * val) % mod
            coef = prime * coef % mod

            if hash1 == hash2:
                longest = i

        return s[:longest:-1] + s
        
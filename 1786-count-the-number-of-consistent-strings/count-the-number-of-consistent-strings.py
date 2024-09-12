class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for word in words:
            isAllow = 1
            for l in word:
                if l not in allowed:
                    isAllow = 0
                    break
            res += isAllow
        return res
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        misMatched = 0
        for l in s:
            if l == "(":
                count += 1
            elif l == ")":
                count -= 1
                if count < 0:
                    misMatched += abs(count)
                    count = 0
        return abs(count) + misMatched
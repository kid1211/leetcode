class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        left = right = 0
        sn = len(s)
        tn = len(t)

        while left < sn and right < tn:
            if s[left] == t[right]:
                right += 1
            left += 1

        return tn - right
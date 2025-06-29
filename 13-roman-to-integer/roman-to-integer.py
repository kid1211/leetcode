class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0        
        for i in range(len(s)):
            l = s[i]

            if i > 0 and maps[s[i]] > maps[s[i - 1]]:
                # you wanna go back
                res -= 2 * maps[s[i - 1]]

            res += maps[l]
        return res
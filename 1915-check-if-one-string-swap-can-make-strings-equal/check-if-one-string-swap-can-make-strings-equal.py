class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        n = len(s1)

        misMatch = ""
        haveSwitched = False
        for i in range(n):
            if s1[i] == s2[i]:
                continue

            if haveSwitched:
                return False

            if not misMatch:
                misMatch = s2[i] + s1[i]
                continue

            if s1[i] + s2[i] == misMatch:
                haveSwitched = True
                misMatch = ""
                continue
            
            return False
        
        return not misMatch
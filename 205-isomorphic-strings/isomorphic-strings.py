class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for i in range(len(s)):
            if (not s[i] in map_s) and (not t[i] in map_t):
                map_s[s[i]] = t[i]
                map_t[t[i]] = s[i]
            elif map_s.get(s[i]) != t[i] or map_t.get(t[i]) != s[i]:
                return False
        return True

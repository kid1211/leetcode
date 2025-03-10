class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        u1, u2 = Counter(word1), Counter(word2)
        # print(u1, u2)
        if u1.keys() != u2.keys():
            return False
        return Counter(u1.values()) == Counter(u2.values())

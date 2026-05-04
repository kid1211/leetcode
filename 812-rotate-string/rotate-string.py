class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # number = "1234"
        # num = 0
        # for i in range(len(number)):
        #     num += int(number[i]) * 10 ** (4 - i)
        # print(num)

        # print(self.find("abc", "abc"))
        # print(self.find("abc", "abcd"))
        # print(self.find("abc", "eabc"))
        # print(self.find("abc", "dfdsfcabcfff"))
        # print(self.find("abc", "cadbc"))

        return self.find(goal, s+s) and len(goal) == len(s)

    def find(self, needle, haystack) -> bool:

        PRIME = 31
        MOD = sys.maxsize // PRIME
        srcLength = len(needle)

        def getVal(c):
            return ord(c) - ord("a")

        def add(hashval, letter):
            hashval *= PRIME
            hashval += getVal(letter)
            hashval %= sys.maxsize // PRIME
            return hashval

        srcHash = tgtHash = 0
        for i in range(srcLength):
            srcHash = add(srcHash, needle[i])
            tgtHash = add(tgtHash, haystack[i])

        if srcHash == tgtHash:
            return True
        # src abc 3
        # tgt cabc 4
        coef = PRIME ** (srcLength - 1)

        for i in range(srcLength, len(haystack)):
            # print(i, dst[i: i + srclength])
            # print(i, dst)
            # print(haystack[i- srcLength],)
            tgtHash -= getVal(haystack[i- srcLength]) * coef
            tgtHash = add(tgtHash, haystack[i])
            if srcHash == tgtHash:
                return True
        return False
            
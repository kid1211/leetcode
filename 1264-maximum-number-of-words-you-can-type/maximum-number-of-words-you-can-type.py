class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)

        res = 0
        for letter in text.split(" "):
            if not set(letter).intersection(broken):
                res += 1
        return res
                
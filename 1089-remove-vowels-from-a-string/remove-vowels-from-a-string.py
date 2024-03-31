class Solution:
    def removeVowels(self, s: str) -> str:
        vowel = set("aeiou")
        return "".join([l for l in s if l not in vowel])
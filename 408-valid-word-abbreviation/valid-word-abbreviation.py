class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        number = []
        word = word + "a"
        abbr = abbr + "a"
        
        j = 0 # word
        for i in range(len(abbr)):
            c = abbr[i]
            if c.isnumeric():
                number += [c]
                continue

            if number and number[0] == "0":
                return False
    
            tmp = int("".join(number)) if number else 0
            j += tmp
            if j >= len(word) or abbr[i] != word[j]:
                return False
            j += 1
            number = []

        return len(word) == j

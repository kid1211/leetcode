class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def shift(word, delta):
            word = list(word)
            for i in range(len(word)):
                word[i] = chr((ord(word[i]) - delta) % 26)
            return "".join(word)
        
        unique = defaultdict(list)
        for word in strings:
            delta = ord(word[0]) - ord('a')
            unique[shift(word, delta)] += [word]
        
        return unique.values()
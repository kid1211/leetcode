class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        right = None
        for i in range(len(word)):
            if word[i] == ch:
                right = i
                break
        if not right:
            return word
        
        left = 0
        word = list(word)
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return "".join(word)
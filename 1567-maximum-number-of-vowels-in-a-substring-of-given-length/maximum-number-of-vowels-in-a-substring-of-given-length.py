class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # maps = defaultdict(int)
        vowels = set('aeiou')
        running = 0

        for i in range(k - 1):
            if s[i] in vowels:
                running += 1
        
        res = 0
        for i in range(k - 1, len(s)):
            if s[i] in vowels:
                running += 1
            res = max(res, running)
            if s[i - k + 1] in vowels:
                running -= 1
        return res
        
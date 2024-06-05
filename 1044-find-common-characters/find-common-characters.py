class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        res = Counter(words[0])

        for i in range(1, len(words)):
            last, res = res, Counter()
            curr = Counter(words[i])

            for l in curr:
                if l in last:
                    res[l] = min(curr[l], last[l])


        return [l for l in res for _ in range(res[l])]
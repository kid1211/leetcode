class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(201):
            matched = None
            for word in strs:
                if i >= len(word):
                    return res

                if matched is None:
                    matched = word[i]
                elif matched != word[i]:
                    return res
            res += matched
        return res

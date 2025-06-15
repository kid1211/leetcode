class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @cache
        def dfs(i1, i2):
            if i2 >= len(word2):
                # remove remainig
                # print((i1, len(word1)), (i2, len(word2)))
                return max(len(word1) - i1, 0)

            if i1 >= len(word1):
                # add reemaining
                # print((i1, len(word1)), (i2, len(word2)))
                return max(len(word2) - i2, 0) # TODO: might not necessary

            if word1[i1] == word2[i2]:
                return dfs(i1 + 1, i2 + 1)
            else:
                return 1 + min(
                    dfs(i1 + 1, i2),
                    dfs(i1 + 1, i2 + 1),
                    dfs(i1, i2 + 1)
                )
        return dfs(0, 0)
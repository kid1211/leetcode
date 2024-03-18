class Solution:
    def maxLength(self, arr: List[str]) -> int:
        newArr = []
        for item in arr:
            candiate = set(item)
            length = len(candiate)
            if len(item) == length:
                newArr += [(candiate, length)]

        # combination
        def dfs(startIdx, curr):
            if startIdx >= len(newArr):
                return 0

            res = 0
            for i in range(startIdx, len(newArr)):
                if newArr[i][0].intersection(curr):
                    continue

                for key in newArr[i][0]:
                    curr.add(key)

                res = max(res, newArr[i][1] + dfs(i + 1, curr))

                for key in newArr[i][0]:
                    curr.remove(key)

            return res
        return dfs(0, set())
# 16

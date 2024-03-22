class Solution:
    def maxLength(self, arr: List[str]) -> int:
        newArr = []

        for item in arr:
            tmp = set(item)
            if len(tmp) == len(item):
                newArr += [tmp]

        def dfs(startIdx, unique):
            if startIdx >= len(newArr):
                return 0
            
            res = 0
            for i in range(startIdx, len(newArr)):
                if unique.intersection(newArr[i]):
                    continue
                for key in newArr[i]:
                    unique.add(key)
                res = max(res, len(newArr[i]) + dfs(i + 1, unique))
    
                for key in newArr[i]:
                    unique.remove(key)
            
            return res

        return dfs(0, set())
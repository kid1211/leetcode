class Solution:
    def maxLength(self, arr: List[str]) -> int:
        newArr = []

        for item in arr:
            tmpSet = set(item)
            if len(tmpSet) != len(item):
                continue
            newArr += [tmpSet]
        
        def dfs(startIdx, currSet):
            if startIdx >= len(arr):
                return 0
            
            res = 0
            for i in range(startIdx, len(newArr)):
                if currSet.intersection(newArr[i]):
                    continue
                
                for key in newArr[i]:
                    currSet.add(key)
                
                res = max(res, len(newArr[i]) + dfs(i + 1, currSet))

                for key in newArr[i]:
                    currSet.remove(key)
            return res
        
        return dfs(0, set())
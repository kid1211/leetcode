class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # if not queries

        res = [ -1 for _ in range(len(queries))]
        # rearrange the queries base on the idx of right element
        # because we can only go right
        newQueries = [ [] for _ in range(len(heights))]

        for i in range(len(queries)):
            a, b = queries[i]

            if a > b:
                a, b = b, a
            
            if heights[b] > heights[a] or a == b:
                res[i] = b
            else:
                newQueries[b] += [(heights[a], i)]

        def findLeftMostElementThatIsGreaterThanOrEqual(target):
            if not mono:
                return -1

            left, right = 0, len(mono) - 1
            while left + 1 < right:
                mid = (left + right) // 2

                if mono[mid][0] <= target:
                    right = mid
                else:
                    left = mid
            if mono[right][0] > target:
                return right
            elif mono[left][0] > target:
                return left
            else:
                return -1

        def buildAns(i):
            for height, qIdx in newQueries[i]:
                pos = findLeftMostElementThatIsGreaterThanOrEqual(height)
                if pos != -1:
                    res[qIdx] = mono[pos][1]

        mono = []
        for i in range(len(newQueries) - 1, -1, -1):
            buildAns(i)
            while mono and mono[-1][0] <= heights[i]:
                mono.pop()
            mono += [(heights[i], i)]
            # print(mono)
        # print(newQueries)
        return res

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        jobs = sorted([
            (startTime[i], endTime[i], profit[i]) for i in range(n)
        ])

        def binary_search(left, right, target):
            while left + 1 < right:
                mid = (left + right) // 2
                if jobs[mid][0] < target:
                    left = mid
                else:
                    right = mid

            if left > right:
                return n
            elif jobs[left][0] >= target:
                return left
            elif jobs[right][0] >= target:
                return right
            return n

        nextTime = [binary_search(i + 1, n - 1, jobs[i][1]) for i in range(n)]

        @cache
        def dfs(curr):
            if curr == n:
                return 0
            return max(
                dfs(curr + 1),
                dfs(nextTime[curr]) + jobs[curr][2]
            )
        
        return dfs(0)
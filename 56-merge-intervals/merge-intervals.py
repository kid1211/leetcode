class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for start, end in intervals:
            if res and res[-1][1] >= start:
                ls, le = res.pop()
                res += [[ls, max(le, end)]]
            else:
                res += [[start, end]]
        return res
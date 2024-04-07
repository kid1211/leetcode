class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        for start, end in sorted(intervals):
            if not res or start > res[-1][1]:
                res += [[start, end]]
            else:
                prevStart, prevEnd = res.pop()
                res += [[
                    min(start, prevStart), max(end, prevEnd)
                ]]
        return res
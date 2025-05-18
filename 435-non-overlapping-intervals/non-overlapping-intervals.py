class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        # print(intervals)
        curr = - sys.maxsize
        res = 0
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start >= curr:
                curr = end
            else:
                res += 1
        return res
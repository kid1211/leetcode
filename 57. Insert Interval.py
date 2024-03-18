class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        for start, end in intervals:
            if newInterval and newInterval[1] < start:
                res += [newInterval]
                res += [[start, end]]
                newInterval = None
                continue

            if not newInterval or newInterval[0] > end or newInterval[1] < start:
                res += [[start, end]]
            else:
                newInterval = [
                    min(newInterval[0], start),
                    max(newInterval[1], end)
                ]

        # [[1, 5]] [[6, 6]]
        if newInterval:
            res += [newInterval]

        return res

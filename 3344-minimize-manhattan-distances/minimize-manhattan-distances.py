from sortedcontainers import SortedList
DELTA = [(1, 1), (-1, 1),  (1, -1), (-1, -1)]
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        pts = [SortedList() for _ in range(4)]

        for x, y in points:
            i = 0
            for dx, dy in DELTA:
                pts[i] += [x * dx + y * dy]
                i += 1

        ret = sys.maxsize

        for x, y in points:
            for i in range(4):
                dx, dy = DELTA[i]
                pts[i].remove(x * dx + y * dy)

            res = 0
            for sortedlist in pts:
                res = max(res, sortedlist[-1] - sortedlist[0])
            ret = min(ret, res)

            for i in range(4):
                dx, dy = DELTA[i]
                pts[i] += [x * dx + y * dy]

        return ret
            
        
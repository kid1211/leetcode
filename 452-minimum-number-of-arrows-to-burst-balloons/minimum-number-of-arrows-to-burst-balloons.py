class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        res = []
        for start, end in sorted(points):
            if not res or start > res[-1][1]:
                res += [(start, end)]
            else:
                ls, le = res.pop()
                res += [(
                    max(start, ls),
                    min(end, le)
                )]
            # print(res)
        # print(res)
        return len(res)

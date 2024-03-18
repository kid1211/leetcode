class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = []
        for start, end in sorted(points, key=lambda item: item[1]):
            if res and start <= res[-1] <= end:
                # already poped
                continue
            res += [end]
        return len(res)

# 1 ------ 6
#    2--4
    
# 1 ------ 6
#    2-------- 7

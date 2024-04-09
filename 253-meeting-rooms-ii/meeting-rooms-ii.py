class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pts = []
        for start, end in intervals:
            pts += [(start, 1)]
            pts += [(end, -1)]
        
        res = curr = 0
        for _, delta in sorted(pts):
            curr += delta
            res = max(res, curr)
        return res
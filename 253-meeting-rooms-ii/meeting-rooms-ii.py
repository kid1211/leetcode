class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pts = []

        for start, end in intervals:
            pts += [(start, 1)]
            pts += [(end, -1)]
        
        res = rolling = 0
        for _, delta in sorted(pts):
            rolling += delta
            res = max(res, rolling)
        return res
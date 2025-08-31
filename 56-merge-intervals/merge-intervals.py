# Tible knowledge: how sorting work for the tuple, see first and be first
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        for start, end in sorted(intervals):
            if res and res[-1][1] >= start:
                ls, le = res.pop()
                res += [[
                    min(start, ls),
                    max(end, le)
                ]]
            else:
                res += [[start, end]]
        return res

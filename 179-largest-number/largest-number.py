class SortableStr(str):
    def __lt__(self, nxtVal):
        return self + nxtVal < nxtVal + self
        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=lambda item: SortableStr(item), reverse=True)
        res = ""
        for item in nums:
            if res == 0 and item == 0:
                continue
            res += str(item)
        return res if res[0] != '0' else '0'
    # 3 30
    # 313
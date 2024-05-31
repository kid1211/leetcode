class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        unique = set()
        for num in nums:
            if num in unique:
                unique.remove(num)
            else:
                unique.add(num)
        return list(unique)
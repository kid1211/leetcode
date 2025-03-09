class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        top = max(candies)

        res = []
        for can in candies:
            res += [True if can + extraCandies >= top else False]
        return res
# 1. valley point is easy, it will always be 1 at the valley
# 2. however local peak is diffcult in the sense that, it is determined by both side

# with that in mind, that is why, we can finally calculate or finalized the assignment after we gone through a segment that increase first then decrease, or in other word, both side of the local peak. Only then, we can knoow what is the peak, which subsequently finalized how we asign value.

# I think this is it, do you understand what I am saying? if so, summarized all the things in this sesession, and explain to me why we count inc first then dec
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        ret = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ret[i] = ret[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                ret[i] = max(ret[i], ret[i + 1] + 1)
        return sum(ret)
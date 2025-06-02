

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
                # ret[i] = ret[i + 1] + 1 
                ret[i] = max(ret[i], ret[i + 1] + 1)
                # [12,4,3, 11, 34, 34, 1, 67]
        return sum(ret)
# 1. valley point is easy, it will always be 1 at the valley
# 2. however local peak is diffcult in the sense that, it is determined by both side

# with that in mind, that is why, we can finally calculate or finalized the assignment after we gone through a segment that increase first then decrease, or in other word, both side of the local peak. Only then, we can knoow what is the peak, which subsequently finalized how we asign value.

# I think this is it, do you understand what I am saying? if so, summarized all the things in this sesession, and explain to me why we count inc first then dec
class Solution:
    def candy(self, ratings: List[int]) -> int:
        def count(start, end, n):
            return(n*(start + end))//2
        def count_zero_based(n):
            return count(0, n - 1, n)
        
        # do the same question in 0 based first
        # then add the # of children to satisfy the quesiton

        children = len(ratings)
        candies, i = 0, 1
        while i < children:
            inc = dec = 0

            while i < children and ratings[i] > ratings[i-1]:
                inc += 1
                i += 1

            while i < children and ratings[i] < ratings[i-1]:
                dec += 1
                i += 1
                
            # print(inc, dec, i, candies)
            if inc or dec:
                # don't know inc is longer or dec is longer, so just add up to inc or dec, 
                # then add either inc or dec
                candies += count_zero_based(inc) + max(inc, dec) + count_zero_based(dec)
                # print(count_zero_based(inc), max(inc, dec), count_zero_based(dec))
            else:
                # if it is neither, then adding one will be sufficint which will be cover in candies + chilren
                # turning 0 based to 1 based
                i += 1
        return candies + children
class Solution:
    def candy(self, ratings: List[int]) -> int:
        def count(start, end, n):
            return(n*(start + end))//2
        def count_zero_based(n):
            return count(0, n - 1, n)
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
                # don't know inc is longer or dec is longer, so just add up to inc or dec, then add either in or dec
                candies += count_zero_based(inc) + max(inc, dec) + count_zero_based(dec)
                # print(count_zero_based(inc - 1), max(inc, dec), count_zero_based(dec - 1))
                # candies += count()
            else:
                i += 1
        return candies + children
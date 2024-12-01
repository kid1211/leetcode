class Solution:
    # Function to calculate sum of first n natural numbers
    def count(self, n):
        return (n * (n + 1)) // 2

    def candy(self, ratings):
        if len(ratings) <= 1:
            return len(ratings)
        candies = 1
        up = 0
        down = 0
        oldSlope = 0
        for i in range(1, len(ratings)):
            newSlope = (
                1
                if ratings[i] > ratings[i - 1]
                else (-1 if ratings[i] < ratings[i - 1] else 0)
            )
            # slope is changing from uphill to flat or downhill
            # or from downhill to flat or uphill
            if (oldSlope > 0 and newSlope == 0) or (
                oldSlope < 0 and newSlope >= 0
            ):
                candies += self.count(up) + self.count(down) + max(up, down)
                up = 0
                down = 0
            # slope is uphill
            if newSlope > 0:
                up += 1
            # slope is downhill
            elif newSlope < 0:
                down += 1
            # slope is flat
            else:
                candies += 1
            oldSlope = newSlope
        candies += self.count(up) + self.count(down) + max(up, down)
        return candies
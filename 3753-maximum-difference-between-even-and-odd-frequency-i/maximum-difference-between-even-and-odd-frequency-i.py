class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)

        largestOdd = -sys.maxsize
        smallestEven = sys.maxsize
        for char in counter:
            freq = counter[char]

            if freq % 2 == 0:
                smallestEven = min(smallestEven, freq)
            else:
                largestOdd = max(largestOdd, freq)
        
        return largestOdd - smallestEven
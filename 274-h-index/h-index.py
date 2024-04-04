class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        return 0
# 0, 1, 3, 6, 5
# 1, 1, 3
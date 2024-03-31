from sortedcontainers import SortedList
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        delta = [
            (1, 1, 1), 
            (1, -1, 1), 
            (1, -1, -1), 
            (1, 1, -1),
            (-1, 1, 1), 
            (-1, -1, 1), 
            (-1, -1, -1), 
            (-1, 1, -1)
        ]
        n = len(delta)
        pts = [SortedList() for _ in range(n)]
        # pts = [SortedList()] * n

        for idx in range(len(arr1)):
            for i in range(n):
                dx, dy, dz = delta[i]
                pts[i] += [arr1[idx] * dx + arr2[idx] * dy + idx * dz]

        return max(
            item[-1] - item[0] for item in pts 
        )
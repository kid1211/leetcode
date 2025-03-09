class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def isEmpty(idx):
            return idx < 0 or idx >= len(flowerbed) or flowerbed[idx] == 0

        for i in range(len(flowerbed)):
            if flowerbed[i] != 0:
                continue
            left, right = i - 1, i + 1

            if isEmpty(left) and isEmpty(right):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break
        return n <= 0

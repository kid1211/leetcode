# Trible 1
    #    if self.w[left] >= target:
    #         return left
    #     else:
    #         return right
# Trible 2, uniform
class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w
        print(self.w)

    def pickIndex(self) -> int:
        if not self.w:
            return -1
        target = uniform(0, self.w[-1]) # maybe +1
        
        left, right = 0, len(self.w) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if self.w[mid] < target:
                left = mid
            else:
                right = mid
        # [1, 5, 15, 17,20]
        if self.w[left] >= target:
            return left
        else:
            return right
        
    # def pickIndex(self) -> int:
    #     target = random.uniform(0, self.w[-1])
    #     start, end = 0, len(self.w) - 1
        
    #     while start + 1 < end:
    #         mid = (start + end) // 2
            
    #         if self.w[mid] >= target:
    #             end = mid
    #         else:
    #             start = mid
        
    #     return start if self.w[start] >= target else end
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# [1 , 4, 10, 2, 3]
# [1, 5, 15, 17,20] # rand(0, 20) => 6
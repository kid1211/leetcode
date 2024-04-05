class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        length = [(1, 1)] * n
        last = (1, 1)
        for i in range(1, len(nums)):
            left, right = length[i]
            prevLeft, prevRight = last
            if nums[i] <= nums[i - 1]:
                length[i] = (prevLeft + 1, right)
            else:
                length[i] = (1, right)
            last = length[i]

        last = (1, 1)
        for i in range(len(nums) - 2, -1, -1):
            left, right = length[i]
            prevLeft, prevRight = last
            if nums[i] <= nums[i + 1]:
                length[i] = (left, prevRight + 1)
            else:
                length[i] = (left, 1)
            last = length[i]
        
        # print(length)
        res = []
        for i in range(1, n - 1):
            prevLeft, prevRight = length[i - 1]
            nextLeft, nextRight = length[i + 1]
            # print(i, left, right)
            if prevLeft >= k and nextRight >= k:
                res += [i]
        
        # last = nums[0]
        # test = ["0"]
        # for num in nums[1:]:
        #     test += "+" if num >= last else "-"
        #     last = num
        # print(test)
        return res
# ['0', '-', '-', '-', '-', '+', '+', '+', '+', '+']
# [(1, 1), (2, 1), (3, 1), (4, 1), (5, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1)]

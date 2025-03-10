class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        for num in nums:
            if k - num == num and num in counter:
                if counter[num] >= 2:
                    res += 1
                    counter[num] -= 2
                    if counter[num] == 0:
                        del counter[num]
            elif k - num in counter and num in counter:
                res += 1
                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]
                counter[k - num] -= 1
                if counter[k - num] == 0:
                    del counter[k - num]
        return res
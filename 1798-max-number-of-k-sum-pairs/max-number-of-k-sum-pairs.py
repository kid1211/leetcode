class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        for num in nums:
            cond1 = k - num == num and num in counter and counter[num] >= 2
            cond2 = k - num != num and k - num in counter and num in counter
            if cond1 or cond2:
                res += 1
                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]
                counter[k - num] -= 1
                if counter[k - num] == 0:
                    del counter[k - num]
        return res
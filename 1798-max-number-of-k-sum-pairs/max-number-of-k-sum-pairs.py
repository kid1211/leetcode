class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        res = 0
        def update():
            nonlocal res
            res += 1
            counter[num] -= 1
            if counter[num] == 0:
                del counter[num]
            counter[k - num] -= 1
            if counter[k - num] == 0:
                del counter[k - num]
    
        for num in nums:
            cond1 = k - num == num and num in counter and counter[num] >= 2
            cond2 = k - num in counter and num in counter
            if k - num == num and num in counter:
                if counter[num] >= 2:
                    update()
            elif k - num in counter and num in counter:
                update()
            # if (
            #      and counter[num] >= 2 or
            #     k - num != num and k - num in counter and num in counter
            #     ):
            # if k - num == num and num in counter:
            #     if counter[num] >= 2:
            #         res += 1
            #         counter[num] -= 2
            #         if counter[num] == 0:
            #             del counter[num]
            # elif k - num in counter and num in counter:
        return res
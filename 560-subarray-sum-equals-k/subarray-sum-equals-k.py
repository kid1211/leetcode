class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # cannot use set, [1,-1,0]
        maps = defaultdict(int)
        maps[0] = 1
        rolling = 0
        res = 0
        for num in nums:
            rolling += num
            if rolling - k in maps:
                res += maps[rolling - k]
            maps[rolling] += 1
            # print(rolling, maps)
        return res

        # n = len(nums)
        # res = right = cumulate = 0

        # for left in range(n):
        #     while right < n and cumulate < k:
        #         cumulate += nums[right]
        #         right += 1

        #     if right > left and cumulate == k:
        #         res += 1

        #     cumulate -= nums[left]
        # return res


        # def dfs(startIdx, target):
        #     if startIdx >= len(nums):
        #         return 0

        #     res = 0
        #     for i in range(startIdx, len(nums)):
        #         nextTarget = target - nums[i]
        #         if nextTarget < 0:
        #             continue # BREAK?
        #         # if nextTarget == 0:
        #         #     res += 1
        #         res += dfs(i + 1, nextTarget)

        #     if target == 0:
        #         res += 1
        #     return res

        # return dfs(0, k)

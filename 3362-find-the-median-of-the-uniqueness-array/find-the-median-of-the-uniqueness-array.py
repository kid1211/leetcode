class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2

        def halfSubArraySmaller(x):
            res = 0
            for start in range(len(nums)):
                hashset = set()
                for end in range(start, len(nums)):
                    hashset.add(nums[end])
                    if len(hashset) <= x:
                        res += 1
                        print(start, end)
                    if res >= (total + 1) // 2:
                        return True
            return False

        def helper(x):
            unique = Counter()
            res = left = 0
            for right in range(len(nums)):
                unique[nums[right]] += 1
                while len(unique) > x:
                    unique[nums[left]] -= 1
                    if unique[nums[left]] == 0:
                        del unique[nums[left]]
                    left += 1
                # print(left, right)
                res += right - left + 1
            return res >= (total + 1) // 2
        # print(halfSubArraySmaller(0))
        # print(helper(2))
        # return 0

        left, right = 1, (total + 1) // 2
        while left + 1 < right:
            mid = (left + right) // 2

            if helper(mid):
                right = mid
            else:
                left = mid

        return left if helper(left) else right

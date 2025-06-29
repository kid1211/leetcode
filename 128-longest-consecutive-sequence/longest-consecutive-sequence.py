class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [1, 2, 4, 5, 7, 8, 10, 11]

        unique = set(nums)
        longest = 0


        for key in unique:
            # make sure we always start with the largest
            if key + 1 in unique:
                continue

            res = 1
            while key - 1 in unique:
                res += 1
                key -= 1

            longest = max(longest, res)
        return longest


# 4 2 1 3

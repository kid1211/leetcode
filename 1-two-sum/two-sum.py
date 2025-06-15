class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in hashmap:
                hashmap[target - num] = i
            else:
                return [
                    hashmap[num], i
                ]
        return None
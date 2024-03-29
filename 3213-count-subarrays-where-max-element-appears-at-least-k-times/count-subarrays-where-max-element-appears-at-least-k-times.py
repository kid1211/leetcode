class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        counter = defaultdict(int)

        left = res = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1
            while left <= right and counter[maxElement] == k:
                counter[nums[left]] -= 1
                left += 1
            # if counter[maxElement] >= k:
            #     print(left, right)
            res += left
                
        # 1, 3
        return res

# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         max_element = max(nums)
#         ans = start = max_elements_in_window = 0

#         for end in range(len(nums)):
#             if nums[end] == max_element:
#                 max_elements_in_window += 1
#             while max_elements_in_window == k:
#                 if nums[start] == max_element:
#                     max_elements_in_window -= 1
#                 start += 1
#             ans += start
#         return ans
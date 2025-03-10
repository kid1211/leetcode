class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique1, unique2 = set(nums1), set(nums2)
        
        def get_diff(left, right):
            temp = []
            for item in left:
                if item not in right:
                    temp += [item]
            return temp

        return [
            get_diff(unique1, unique2),
            get_diff(unique2, unique1),
        ]
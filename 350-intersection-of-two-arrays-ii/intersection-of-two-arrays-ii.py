class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l, r = Counter(nums1), Counter(nums2)

        res = []
        for key in l:
            if key not in r:
                continue
            res += [key for _ in range(min(l[key], r[key]))]
        return res
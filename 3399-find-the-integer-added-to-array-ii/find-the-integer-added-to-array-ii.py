class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        def checkIfMatch(start):
            skipped = start
            diff = nums2[0] - nums1[start]
            i2 = 1
            for i in range(start + 1, len(nums1)):
                if i2 == len(nums2):
                    print(skipped, 2 - skipped, len(nums1) - i, len(nums1), i)
                    return 2 - skipped == len(nums1) - i

                if nums2[i2] - nums1[i] != diff:
                    skipped += 1
                else:
                    i2 += 1

                if skipped > 2:
                    return False
            return True

        min2 = min(nums2)
        res = sys.maxsize
        for i in range(3):
            if checkIfMatch(i):
                res = min(res, min2 - nums1[i])
        return res

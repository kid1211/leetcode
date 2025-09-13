class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r = m - 1, n - 1
        idx = m + n - 1

        while l >= 0 or r >= 0:
            lVal = nums1[l] if l >= 0 else -sys.maxsize
            rVal = nums2[r] if r >= 0 else -sys.maxsize

            if lVal > rVal:
                nums1[idx] = lVal
                l -= 1
            else:
                nums1[idx] = rVal
                r -= 1
            idx -= 1
        
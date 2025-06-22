class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1
        while k >= 0:
            n1 = nums1[i] if i >= 0 else -sys.maxsize
            n2 = nums2[j] if j >= 0 else -sys.maxsize
            if n1 > n2:
                val = nums1[i]
                i -= 1
            else:
                val = nums2[j]
                j -= 1
            nums1[k] = val
            k -= 1


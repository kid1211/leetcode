class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def helper(i, min_limit, max_limit):
            if i == len(preorder):
                return i, True
            
            root = preorder[i]
            if not min_limit < root < max_limit:
                return i, False

            leftIdx, left = helper(i + 1, min_limit, root)
            rightIdx, right = helper(leftIdx, root, max_limit)
            return rightIdx, left or right
            
        return helper(0, -inf, inf)[1]
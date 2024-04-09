# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node) -> (int, int):
            nonlocal res
            if not node:
                return 0
            
            leftLength = dfs(node.left)
            rightLength = dfs(node.right)
            res = max(res, leftLength + rightLength)
            return max(leftLength, rightLength) + 1
        dfs(root)
        return res
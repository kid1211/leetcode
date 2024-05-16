# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return False
            if not node.left and not node.right:
                return True if node.val == 1 else False

            left = dfs(node.left)
            right = dfs(node.right)

            return (left or right) if node.val == 2 else (left and right)

        return dfs(root)

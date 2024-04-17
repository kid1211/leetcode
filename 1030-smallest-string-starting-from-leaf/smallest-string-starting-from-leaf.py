# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def getLetter(val):
            return chr(val + ord('a'))

        res = []
        def dfs(node, prefix):
            nonlocal res
            if not node:
                return

            if not node.left and not node.right:
                res += [prefix[::-1]]
                return

            if node.left:
                dfs(node.left, prefix + getLetter(node.left.val))
            if node.right:
                dfs(node.right, prefix + getLetter(node.right.val))
        dfs(root, getLetter(root.val))
        return min(res)
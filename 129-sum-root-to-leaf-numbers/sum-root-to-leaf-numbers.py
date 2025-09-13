# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = []
        def dfs(curr, node):
            nonlocal total
            
            curr += str(node.val)
            if not node.left and not node.right:
                total += [int(curr)]
            if node.left:
                dfs(curr, node.left)
            if node.right:
                dfs(curr, node.right)

        dfs("", root)
        if not root:
            return 0
        return sum(total)
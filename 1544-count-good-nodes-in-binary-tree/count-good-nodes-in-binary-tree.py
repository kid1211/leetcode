# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxi):
            nonlocal res
            if not node:
                return
            
            if node.val >= maxi:
                res += 1
            newMax = max(maxi, node.val)
            dfs(node.left, newMax)
            dfs(node.right, newMax)
            # root, left, right
        dfs(root, -sys.maxsize + 1)
        return res
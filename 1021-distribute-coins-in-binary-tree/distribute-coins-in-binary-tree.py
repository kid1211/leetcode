# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            res += abs(left) + abs(right)
            return node.val + left + right - 1

        dfs(root)
        return res
    # def distributeCoins(self, root: Optional[TreeNode]) -> int:
    #     res = 0
    #     def dfs(node):
    #         nonlocal res
    #         if not node:
    #             return 0

    #         l = dfs(node.left)
    #         r = dfs(node.right)
    #         res += abs(l) + abs(r)
    #         return node.val + l + r - 1
    #     dfs(root)
    #     return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1

        def dfs(node, curr):
            nonlocal res
            if not node:
                return

            curr += node.val

            # One special case
            # if curr == targetSum:
            #     res += 1

            res += hashmap[curr - targetSum]

            hashmap[curr] += 1
            dfs(node.left, curr)
            dfs(node.right, curr)
            hashmap[curr] -= 1
            return

        dfs(root, 0)
        return res


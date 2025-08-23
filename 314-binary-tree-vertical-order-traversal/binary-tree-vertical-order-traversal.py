# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        maps = {}

        def dfs(node, index, depth):
            if not node:
                return
            if index not in maps:
                maps[index] = {}
            if depth not in maps[index]:
                maps[index][depth] = []
    
            maps[index][depth] += [node.val]
            dfs(node.left, index - 1, depth + 1)
            dfs(node.right, index + 1, depth + 1)

        dfs(root, 0, 0)
        # print(maps)
        res = []
        for key in sorted(maps.keys()):
            tmp = []
            for depth in sorted(maps[key].keys()):
                tmp += maps[key][depth]
            res += [tmp]
        return res

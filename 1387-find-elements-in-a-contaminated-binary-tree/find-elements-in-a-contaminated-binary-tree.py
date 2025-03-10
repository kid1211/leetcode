# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.unique = set()

        def dfs(node):
            if not node:
                return
            self.unique.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                dfs(node.right)
        root.val = 0
        dfs(root)


    def find(self, target: int) -> bool:
        return target in self.unique


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
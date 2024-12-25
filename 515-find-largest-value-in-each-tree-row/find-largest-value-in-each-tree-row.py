# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res
        queue = deque([root])

        while queue:
            localMax = - sys.maxsize
            for _ in range(len(queue)):
                node = queue.popleft()
                localMax = max(localMax, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += [localMax]

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        res = []

        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()

                tmp += [node.val]

                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]
            res += [tmp[-1]]
        return res
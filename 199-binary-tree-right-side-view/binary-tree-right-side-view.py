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
        res = [root.val]
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue += [node.left]
                
                if node.right:
                    queue += [node.right]
            if queue:
                res += [queue[-1].val]
        
        return res

        
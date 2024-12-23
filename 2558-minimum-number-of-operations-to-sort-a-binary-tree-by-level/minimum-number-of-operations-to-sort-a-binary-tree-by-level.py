# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])

        def countSwap(vals):
            sortedVals = sorted(vals)
            val2Pos = { vals[i]: i for i in range(len(vals)) }
            # print(val2Pos)

            res = 0
            for i in range(len(vals)):
                if sortedVals[i] != vals[i]:
                    res += 1

                    left, right = val2Pos[sortedVals[i]], val2Pos[vals[i]]
                    vals[left], vals[right] = vals[right], vals[left]
                    val2Pos[vals[left]] = left
                    val2Pos[vals[right]] = right
            # print(vals)
            return res

        res = 0
        while queue:
            res += countSwap([node.val for node in queue])
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue += [node.left]

                if node.right:
                    queue += [node.right]

        return res

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        
        def dfs(node, newParent):
            # print('before', node.val , newParent.val if newParent else -1)
            # TODO: no node?
            oriParent = node.parent
            node.parent = newParent

            if node == root:
                print(
                node.val, 
                node.left.val if node.left else -1, 
                node.right.val if node.right else -1, 
                node.parent.val if node.parent else -1)
                if node.left == node.parent:
                    node.left = None
                elif node.right == node.parent:
                    node.right = None
                return

            if node.left and node.left != newParent:
                node.right = node.left
            node.left = oriParent
            # print(
            #     node.val, 
            #     node.left.val if node.left else -1, 
            #     node.right.val if node.right else -1, 
            #     node.parent.val if node.parent else -1)
            # if node == root:
            #     return
            dfs(oriParent, node)

        dfs(leaf, None)

        
        return leaf
# 3 5 1 5
# 3 5 1 1
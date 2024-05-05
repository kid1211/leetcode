# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        last = None
        curr = node
        while curr:
            if last:
                last.val = curr.val
            if not curr.next:
                last.next = None
            last = curr
            curr = curr.next

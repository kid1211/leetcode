# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            last = None
            while node:
                nxt = node.next
                node.next = last
                last = node
                node = nxt
            return last

        def skip(node):
            last, curr = None, node
            maxi = 0
            while curr:
                maxi = max(maxi, curr.val)

                if curr.val < maxi:
                    last.next = curr.next
                    nxt = curr.next
                    # curr.next = None
                    curr = nxt
                else:
                    last = curr
                    curr = curr.next
        newHead = reverse(head)
        skip(newHead)
        return reverse(newHead)

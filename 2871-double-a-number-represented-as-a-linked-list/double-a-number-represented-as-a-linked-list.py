# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            last = None
            while node:
                nxt = node.next
                node.next = last
                last = node
                node = nxt
            return last

        def double(node):
            carry = 0
            last = None
            while node:
                newVal = carry + node.val * 2
                carry = newVal // 10
                node.val = newVal % 10
                last = node
                node = node.next

            if carry:
                last.next = ListNode(carry)


        tmp = reverse(head)
        double(tmp)
        return reverse(tmp)

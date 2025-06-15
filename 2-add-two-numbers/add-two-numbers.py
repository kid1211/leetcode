# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = head = ListNode()
        while l1 or l2 or carry:
            newVal = carry

            if l1:
                newVal += l1.val
                l1 = l1.next

            if l2:
                newVal += l2.val
                l2 = l2.next

            res.val = newVal % 10
            carry = newVal // 10

            if l1 or l2 or carry:
                res.next = ListNode()
                res = res.next

        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead = odd = ListNode()
        evenHead = even = ListNode()

        isOdd = True
        while head:
            nextNode = head.next
            head.next = None
            if isOdd:
                odd.next = head
                odd = head
            else:
                even.next = head
                even = head
    
            isOdd = not isOdd
            head = nextNode

        odd.next = evenHead.next
        return oddHead.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort(head):
            if not head:
                return None
            if not head.next:
                return head
            
            fast = slow = head
            while fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            
            nxt = slow.next
            slow.next = None

            left = sort(head)
            right = sort(nxt)

            dummy = curr = ListNode()
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            
            if left:
                curr.next = left
                curr = curr.next
            elif right:
                curr.next = right
                curr = curr.next
            
            return dummy.next
        sortedList = sort(head)
 
        count = 0
        node = sortedList
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
                count += 1
            else:
                node.val = count + 1
                count = 0
                node = node.next
        if node:
            node.val = count + 1
        return sortedList
                
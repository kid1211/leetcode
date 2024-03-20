# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            head = lists[i]
            if not head:
                continue
            heappush(heap, (head.val, i, head))
        
        dummy = curr = ListNode()
        while heap:
            _, idx, head = heappop(heap)

            curr.next = head
            curr = head

            if curr.next:
                heappush(heap, (
                    curr.next.val,
                    idx,
                    curr.next
                ))
        return dummy.next
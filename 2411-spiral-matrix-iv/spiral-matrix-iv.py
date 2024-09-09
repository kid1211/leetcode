# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1 for _ in range(n)] for _ in range(m)]
        delta = (0, 1)
        (x, y) = (0, 0)
        visited = set()

        while head:
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                res[x][y] = head.val
                head = head.next
                visited.add((x, y))
            else:
                dx, dy = delta
                (x, y) = (x - dx, y - dy)
                if delta == (0, 1):
                    delta = (1, 0)
                    
                elif delta == (1, 0):
                    delta = (0, -1)
                elif delta == (0, -1):
                    delta = (-1, 0)
                else:
                    delta = (0, 1)
            dx, dy = delta
            (x, y) = (x + dx, y + dy)
        return res
# class Solution:
#     def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
#         res = [[-1 for _ in range(n)] for _ in range(m)]
#         delta = (0, 1)
#         (x, y) = (0, 0)
#         visited = set()

#         while head:
#             if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
#                 res[x][y] = head.val
#                 head = head.next
#                 visited.add((x, y))
#             else:
#                 dx, dy = delta
#                 (x, y) = (x - dx, y - dy)
#                 if delta == (0, 1):
#                     delta = (1, 0)
#                 elif delta == (1, 0):
#                     delta = (0, -1)
#                 elif delta == (0, -1):
#                     delta = (-1, 0)
#                 else:
#                     delta = (0, 1)
#             dx, dy = delta
#             (x, y) = (x + dx, y + dy)


            
#         return res
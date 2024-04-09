class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(i, tickets[i]) for i in range(len(tickets))])

        i = 0
        while True:
            idx, remain = queue.popleft()
            remain -= 1
            if remain > 0:
                queue += [(idx, remain)]
            else:
                if idx == k:
                    break
            i += 1
        return i + 1

        
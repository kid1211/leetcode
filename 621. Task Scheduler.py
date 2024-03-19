from heapq import heappush, heappop, heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-cnt, task) for task, cnt in Counter(tasks).items()]
        heapify(heap)
        wl = deque()

        res = []
        while heap or wl:
            # check wait list
            # only do once
            # print(res, wl[0] if wl else None, wl[0][0] <= len(res) if wl else None)
            if wl and wl[0][0] <= len(res):
                _, remainCount, task = wl.popleft()
                heappush(heap, (-remainCount, task))

            if not heap and wl:
                res += [None]
                continue
            
            remainCount, task = heappop(heap)
            res += [task]
            # fix the hack for minhack
            remainCount = -remainCount 
            remainCount -= 1

            if remainCount > 0:
                # remainCount is normal Count
                wl.append((len(res) + n , remainCount, task))

        return len(res)

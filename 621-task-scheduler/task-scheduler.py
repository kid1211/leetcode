from heapq import heappush, heappop, heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-cnt, task) for task, cnt in Counter(tasks).items()]
        heapify(heap)
        wl = deque()
        # A -> B, if it is possible
        # if not possible at to a wait list (deque), because the A must be available before b, given the n is the same time for all
        # check wait list first

        res = []
        while heap or wl:
            # check wait list
            # only do once
            # print(res, wl[0] if wl else None, wl[0][0] <= len(res) if wl else None)
            while wl and wl[0][0] <= len(res):
                _, remainCount, task = wl.popleft()
                heappush(heap, (-remainCount, task))
            # print(res, heap, wl)
            if not heap and wl:
                res += [None]
                continue
            
            remainCount, task = heappop(heap)
            res += [task]
            remainCount = -remainCount # fix the hack for minhack
            remainCount -= 1

            if remainCount > 0:
                # ['b', 'a'], wl => 'b': 0 + 2, 'a': 1 + 2
                # 'b', 'a', None, 'b'
                wl.append((len(res) + n , remainCount, task))

        return len(res)
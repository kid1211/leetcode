from heapq import heappush, heappop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        events += [[sys.maxsize, sys.maxsize]]
        res = 0
        heap = []
        current_day  = 0

        for start, end in events:
            while heap and current_day  < start:
                prev_end = heappop(heap)
                if current_day <= prev_end:
                    res += 1
                    # last_day = start
                    current_day  += 1
            current_day = start
            heappush(heap, end)
        return res

'''
[1, 2] [1, 2] [3, 4] [3, 4]

[1, 3] [1, 3] [3, 3] [1, 5] [1, 5]
'''




















# overlap
# temp = []
# for i in range(len(events)):
#     start, end = events[i]
#     temp += [(start, 1, i)]
#     temp += [(end, -1, i)]


# rolling = 0
# overlapped = []

# for ts, delta, index in sorted(temp):
#     rolling += delta
#     # print(ts, delta, index, rolling)
#     if rolling > 1:
#         overlapped += [index]

# print(overlapped)
# return len(events) - len(overlapped)
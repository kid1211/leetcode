from heapq import heappush, heappop
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        firstMin, lastMin = [], []
        leftBound, rightBound = -1, n
        for _ in range(candidates):
            leftBound += 1
            heappush(firstMin, costs[leftBound])
        # [1, 2, 3, 4] 4 - 2
        for _ in range(candidates):
            if rightBound - 1 <= leftBound: # could be a problem
                break
                # print('wtf')
            rightBound -= 1
            heappush(lastMin, costs[rightBound])
        # print(firstMin)
        # print(lastMin)
        # print(n, len(firstMin), len(lastMin))

        # print(n, len(firstMin), len(lastMin))
        res = 0
        for _ in range(k):
            # print((firstMin, leftBound), (lastMin, rightBound))
            if lastMin and firstMin and firstMin[0] <= lastMin[0] or not lastMin:
                res += heappop(firstMin)

                if leftBound + 1 < rightBound:
                    leftBound += 1
                    heappush(firstMin, costs[leftBound])
            else:
                res += heappop(lastMin)

                if leftBound < rightBound - 1:
                    rightBound -= 1
                    heappush(lastMin, costs[rightBound])

        return res
# class Solution {
#     public long totalCost(int[] costs, int k, int candidates) {
#         int n = candidates;
#         Queue<Integer> pqLeft = new PriorityQueue<>();
#         Queue<Integer> pqRight = new PriorityQueue<>();
#         int left = -1;
#         int right = costs.length;
#         for(int i=0; i< candidates; ++i) {
#             left++;
#             pqLeft.offer(costs[i]);
#         }
#         for(int i=costs.length - 1; i > left && (costs.length - 1 - i) < candidates; --i) {
#             right--;
#             pqRight.offer(costs[i]);
#         }

#         long cost = 0;
#         for(int i=0; i < k; ++i) {
#             if(pqRight.isEmpty() || (!pqLeft.isEmpty() && pqLeft.peek() <= pqRight.peek())) {
#                 cost += pqLeft.poll();
#                 if(left + 1 < right) {
#                     left++;
#                     pqLeft.offer(costs[left]);
#                 }
#             }else {
#                 cost += pqRight.poll();
#                 if(left < right - 1) {
#                     right--;
#                     pqRight.offer(costs[right]);
#                 }
#             }
#         }
#         return cost;
#     }
# }
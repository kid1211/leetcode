class Solution:
    def makePrefSumNonNegative(self, nums):
        operations = 0
        prefix_sum = 0
        pq = []

        for num in nums:
            # Push negative elements to the min heap.
            if num < 0:
                heapq.heappush(pq, num)

            prefix_sum += num
            # Keep popping from heap until sum becomes non-negative.
            while prefix_sum < 0:
                prefix_sum -= heapq.heappop(pq)
                # Increment the operations required.
                operations += 1

        return operations
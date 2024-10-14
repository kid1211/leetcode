class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0

        # Define a max-heap by using a min-heap with negative values
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)

        while k > 0:
            k -= 1
            # Retrieve the max element (invert the sign because it's stored as negative)
            max_element = -heapq.heappop(max_heap)
            ans += max_element
            # Add one-third of the max element back to the heap. Rounded up using integer division.
            heapq.heappush(max_heap, -math.ceil(max_element / 3))

        return ans
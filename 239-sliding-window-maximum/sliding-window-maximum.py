class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        def add(idx):
            while dq and nums[dq[-1]] < nums[idx]:
                dq.pop()
            dq.append(idx)
        
        def remove(idx):
            if dq[0] == idx:
                dq.popleft()
        
        for i in range(k - 1):
            add(i)
        
        res = []
        for i in range(k - 1, len(nums)):
            add(i)
            res += [nums[dq[0]]]
            remove(i - k + 1)
        
        return res
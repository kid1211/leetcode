from sortedcontainers import SortedList
# fixed size sliding window, because of dist, second array start and last array start is fixed distance
  # result is [first elemnt of the entire array] + window[:(k - 1) + 1] (first k element)
# when we move right pointer, we need to expande the sliding window

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 2  # first and last one is used
        cost = nums.pop(0) # first element is selected regardless
        res = float("inf")
        window = SortedList(nums[:dist])
        
        rtn = defaultdict(int)
        rtn[cost] += 1
        for item in window[:k]:
            rtn[item] += 1
        # print(rtn, window)
        cost += sum(window[:k])

        for i in range(len(nums)):
            if i + dist >= len(nums):
                break
            left, right = nums[i], nums[i + dist]

            window.add(right)
            # if right is smaller, use it as start of the last array
            # if right is bigger, use the previous last element as start
            cost += min(window[k], right) 
            rtn[min(window[k], right)] += 1

            # print('potential', rtn, window, window[k], right)
            res = min(res, cost)

            cost -= min(window[k], left)
            rtn[min(window[k], left)] -= 1
            if rtn[min(window[k], left)] == 0:
                del rtn[min(window[k], left)]
            window.remove(left)

        return res
[1,2,3,4,5,6,7,8,9,10,11,12]
[10,1,2,2,2,1]
10, 1, 2, 1
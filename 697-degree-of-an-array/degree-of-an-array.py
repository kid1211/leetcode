class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # minPos, maxPos
        unique = {}
        
        maxFreq = 0
        maxFreqCanidates = []
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique[nums[i]] = (1, i, i)
            else:
                freq, minPos, maxPos = unique[nums[i]]
                unique[nums[i]] = (freq + 1, min(minPos, i), max(maxPos, i))

            if maxFreq < unique[nums[i]][0]:
                maxFreqCanidates = [nums[i]]
                maxFreq = unique[nums[i]][0]
            elif maxFreq == unique[nums[i]][0]:
                maxFreqCanidates += [nums[i]]
        
        # print(maxFreq, maxFreqCanidates, unique)
        res = len(nums)
        for key in maxFreqCanidates:
            res = min(res, unique[key][2] - unique[key][1] + 1)
        return res
            
            


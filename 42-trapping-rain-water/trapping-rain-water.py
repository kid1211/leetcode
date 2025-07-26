class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        # height += [0] # add last just in case, actually no
        # equal sign

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                popped = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                curr_height = min(height[i], height[stack[-1]]) - height[popped]
                res += distance * curr_height
            stack += [i]
        
        return res
            # pop and calculate
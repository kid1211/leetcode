class Solution:
    def leftmostBuildingQueries(self, heights, queries):
       
        result = [-1 for _ in range(len(queries))]
        new_queries = [[] for _ in range(len(heights))]
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                new_queries[b].append((heights[a], i))
        # new_queries = [[], [(6, 0)], [], [(6, 1)], [(8, 2), (5, 3)], []]

        def build_answer(i):
            mono_stack_size = len(mono_stack)
            for a, b in new_queries[i]:
                position = findSmallestElementThatIsGreatherThan(a) 
                if position < mono_stack_size and position >= 0:
                    result[b] = mono_stack[position][1]
    
        # find the smallest element that is greater than height
        def findSmallestElementThatIsGreatherThan(height):
            if not mono_stack:
                return -1
    
            left, right = 0, len(mono_stack) - 1
            ans = -1
            while left + 1 < right:
                mid = (left + right) // 2

                if mono_stack[mid][0] <= height:
                    right = mid
                else:
                    left = mid
            
            if mono_stack[right][0] > height:
                return right
            elif mono_stack[left][0] > height:
                return left
            else:
                return -1

        def search(height):
            left = 0
            right = len(mono_stack) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if mono_stack[mid][0] > height:
                    ans = max(ans, mid)
                    left = mid + 1
                else:
                    right = mid - 1
            print(mono_stack, ans, height)
            return ans
    
        mono_stack = [] # ?? largest to smallest 7, 2
        for i in range(len(heights) - 1, -1, -1):
            build_answer(i)
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))
        return result


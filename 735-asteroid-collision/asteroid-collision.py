class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if abs(ast) > abs(stack[-1]):
                    stack.pop()
                else:
                    break

            if stack and ast < 0 and stack[-1] > 0 and ast == -stack[-1]:
                stack.pop()
            elif not stack or ast > 0 and stack[-1] < 0 or ast * stack[-1] > 0:
                stack += [ast]
        return stack
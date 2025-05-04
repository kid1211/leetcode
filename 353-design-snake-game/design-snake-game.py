mapping = {
    "R": (0, 1),
    "D": (1, 0),
    "U": (-1, 0),
    "L": (0, -1)
}
class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = [tuple(x) for x in food]
        self.snake = collections.deque([(0, 0)])
        self.snakeSet = set([(0, 0)])
        self.score = 0

    def move(self, direction: str) -> int:
        dx, dy = mapping[direction]
        x, y = self.snake[-1] # head
        nx, ny = x + dx, y + dy

        def isValid(cx, cy):
            return 0 <= cx < self.height and 0 <= cy < self.width and (cx, cy)

        if not isValid(nx, ny):
            return -1

        if self.score < len(self.snake):
            # pop your tail
            tail = self.snake.popleft()
            self.snakeSet.remove(tail)

        if (nx, ny) in self.snakeSet:
            return -1

        self.snakeSet.add((nx, ny))
        self.snake.append((nx, ny))

        if self.score < len(self.food) and (nx, ny) == self.food[self.score]:
            self.score += 1
        return self.score



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
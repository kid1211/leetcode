class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.key2Prev = {}
        self.recent = self.head = Node(-1, -1)

    def get(self, key: int) -> int:
        if key not in self.key2Prev:
            return -1
        self.move2Recent(key)
        return self.recent.val

    def put(self, key: int, value: int) -> None:
        if key in self.key2Prev:
            self.move2Recent(key)
            self.recent.val = value
        else:
            self.addNew(key, value)
    
    def move2Recent(self, key):
        if key == self.recent.key:
            return
        self.addNew(key, self.pop(key))

    
    def addNew(self, key, val):
        node = Node(key, val)

        self.key2Prev[key] = self.recent
        self.recent.next = node
        self.recent = node

        if len(self.key2Prev) > self.size:
            self.pop(self.head.next.key)
    
    def pop(self, key) -> int:
        prev = self.key2Prev[key]
        res = prev.next.val

        del self.key2Prev[key]
        prev.next = prev.next.next
        self.key2Prev[prev.next.key] = prev

        return res


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
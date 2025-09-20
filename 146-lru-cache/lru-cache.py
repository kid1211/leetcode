class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        #  head - node - recent
        self.recent = self.head = Node(-1, -1)
        self.key2Prev = {}

    def get(self, key: int) -> int:
        if key not in self.key2Prev:
            return -1
        self.move2Recent(key)
        return self.recent.val
        
    def move2Recent(self, key):
        if key == self.recent.key:
            return
        self.addNew(key, self.pop(key))

    def addNew(self, key, val):
        node = Node(key, val)

        self.recent.next = node
        self.key2Prev[key] = self.recent
        self.recent = node

        if len(self.key2Prev) > self.capacity:
            self.pop(self.head.next.key)
    
    def pop(self, key):
        prevNode = self.key2Prev[key]
        res = prevNode.next.val

        del self.key2Prev[key]
        prevNode.next = prevNode.next.next
        self.key2Prev[prevNode.next.key] = prevNode 

        return res

    
    def put(self, key: int, value: int) -> None:
        if key not in self.key2Prev:
            self.addNew(key, value)
        else:
            self.move2Recent(key)
            self.recent.val = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
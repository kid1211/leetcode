class HashNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
class MyHashMap:

    def __init__(self):
        self.length = 687
        self.array = [HashNode()] * self.length

    def put(self, key: int, value: int) -> None:
        prevNode = self.getPrevNode(key)

        if prevNode.next and prevNode.next.key == key:
            prevNode.next.val = value
        else:
            prevNode.next = HashNode(key, value)

    def get(self, key: int) -> int:
        prevNode = self.getPrevNode(key)
        return prevNode.next.val if prevNode.next else -1

    def remove(self, key: int) -> None:
        prevNode = self.getPrevNode(key)

        if prevNode.next and prevNode.next.key == key:
            prevNode.next = prevNode.next.next
    
    def getPrevNode(self, key):
        hashKey = key % self.length
        node = self.array[hashKey]
        last = None
        while node and node.key != key:
            last = node
            node = node.next
        return last


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
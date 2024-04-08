class HashNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
class MyHashMap:

    def __init__(self):
        size = 31
        self.array = [HashNode()] * 31
        

    def put(self, key: int, value: int) -> None:
        prevNode = self.getPrevNode(key)
        if not prevNode:
            hashKey = key % 31
            self.array[hashKey] = HashNode(key, value)
            return
        elif prevNode.next and prevNode.next.key == key:
            prevNode.next.val = value
            # exist
        else:
            prevNode.next = HashNode(key, value)

    def get(self, key: int) -> int:
        node = self.getPrevNode(key)
        return node.next.val if node and node.next else -1

    def remove(self, key: int) -> None:
        prevNode = self.getPrevNode(key)

        if prevNode and prevNode.next and prevNode.next.key == key:
            prevNode.next = prevNode.next.next
        else:
            print(prevNode)
    
    def getPrevNode(self, key):
        hashKey = key % 31
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
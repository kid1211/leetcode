class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root

        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
        node.isWord = True

    def _find(self, word):
        node = self.root

        for l in word:
            if l not in node.children:
                return None
            node = node.children[l]
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.isWord

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
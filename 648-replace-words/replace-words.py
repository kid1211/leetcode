class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie(dictionary)

        res = []
        for word in sentence.split():
            prefix = trie.prefix(word)
            res += [prefix] if prefix else [word]
        return " ".join(res)

class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = {}

class Trie:
    def __init__(self, dict):
        self.root = TrieNode()
        for word in dict:
            self.add(word)

    def add(self, word):
        node = self.root

        for l in word:
            if node.word:
                return
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
        node.word = word
        node.children = {}

    def prefix(self, prefix):
        node = self.root
        for l in prefix:
            if l not in node.children:
                break
            node = node.children[l]
        return node.word if node.word else None

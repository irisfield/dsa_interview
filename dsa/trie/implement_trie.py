class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    """208. Implement Trie (Prefix Tree)"""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    """
    The time complexity is O(m) for all three methods, where m is the
    length of the string being searched or inserted.

    The space complexity is O(n * m), where n is the number of words in
    the Trie and m is the average length of the words.
    """

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

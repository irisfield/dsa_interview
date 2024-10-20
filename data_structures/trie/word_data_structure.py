class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    """211. Design Add and Search Words Data Structure"""
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(i, cur):
            if i == len(word):
                return cur.endOfWord

            char = word[i]
            if char == ".":
                for ithChar in cur.children:
                    if dfs(i + 1, cur.children[ithChar]):
                        return True
                return False
            else:
                if word[i] not in cur.children:
                    return False
                return dfs(i + 1, cur.children[word[i]])

        return dfs(0, self.root)

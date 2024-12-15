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
        """
        The time complexity is O(m * 4^n), where m is the length of the
        word and n is the number of '.' characters. For each '.'
        character, all possible children at that level are explored.

        The space complexity is O(m * n), where m is the total number of
        characters added and n is the maximum depth. The trie structure
        stores each character of the words.
        """
        return dfs(0, self.root)

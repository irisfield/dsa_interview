class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

class Solution:
    """212. Word Search II"""

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Intuition:
        Instead of checking if a word can be made for every word,
        check all the words that can be made each with each prefix.
        """
        root = TrieNode()

        for word in words:
            root.insert(word)

        ROWS, COLS = len(board), len(board[0])
        res, path = [], set()

        def dfs(r, c, node, word):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in path or board[r][c] not in node.children):
                return

            path.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.end_of_word:
                res.append(word)

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r + dr, c + dc, node, word)

            path.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        """
        The time complexity is O(W * L + m * n * 4^L), where W is the
        number of words, L is the maximum word length, m * n is the size
        of the board, and 4^L accounts for the possible DFS
        explorations.

        The space complexity is O(W * L + m * n) due to the trie tree,
        DFS recursion stack, and the path set.
        """
        return res

    # Time Limit Exceeded 63/65
    def findWords1(self, board: list[list[str]], words: list[str]) -> list[str]:
        ROWS, COLS = len(board), len(board[0])
        res, path = [], set()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] not in prefix:
                    prefix[board[r][c]] = [(r, c)]
                else:
                    prefix[board[r][c]].append((r, c))

        def dfs(r, c, i, word):  # m * n * 4 ^ m * n
            if i == len(word):
                return True

            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in path or board[r][c] != word[i]):
                return False

            path.add((r, c))

            found = (dfs(r + 1, c, i + 1, word) or
                     dfs(r - 1, c, i + 1, word) or
                     dfs(r, c + 1, i + 1, word) or
                     dfs(r, c - 1, i + 1, word))

            path.remove((r, c))
            return found

        for word in words:
            for c in word:
                if c not in prefix:
                    break
            else:
                for r, c in prefix[word[0]]:
                    if dfs(r, c, 0, word):
                        res.append(word)
                        break
        """
        The time complexity is O(w * m * n * 4^{m * n}), where w is the
        number of words, m * n is the size of the board, and 4^{m * n}
        accounts for the possible DFS explorations.


        The space complexity is O(m * n) due to the DFS recursion stack,
        the path set, and the prefix map. In the worst case, each of them
        can store every cell in the board or their position.
        """
        return res

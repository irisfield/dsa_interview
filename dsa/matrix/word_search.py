class Solution:
    """79. Word Search"""

    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # Iterate through the board
        # Find the first letter of the word in the board
        # Run dfs + backtracking algorithm to find letter by letter

        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in path or
                board[r][c] != word[i]):
                return False

            path.add((r, c))

            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))

            path.remove((r, c))  # backtrack
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        """
        The time complexity is O(n * m * 4 ^ w), where n * m is the size
        of the board and w is the length of the word.

        The space complexity is O(n * m + w), where n * m is the size of
        the board, and w is the length of the word. This accounts for
        the recursion call stack and the set used for the path.
        """
        return False

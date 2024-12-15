class Solution:
    """51. N-Queens"""

    def solveNQueens(self, n: int) -> list[list[str]]:
        # Decision tree for n choices
        cols = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)
        res = []
        board = [["."] * n for _ in range(n)]  # n x n board

        def backtrack(r):
            if r == n:  # all queens were successfully placed
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if (c in col or
                    (r + c) in posDiag or
                    (r - c) in negDiag):
                    continue
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)

        """
        The time complexity is O(n!), as the algorithm explores all
        possible valid ways to place queens on the board, which can be
        as many as n!.

        The space complexity is O(n^2 + n!), as the space is used by the
        board O(n^2)), recursion stack (O(n)), and the solutions
        (O(n!)), so the overall space complexity is O(n^2 + n!).
        """
        return res

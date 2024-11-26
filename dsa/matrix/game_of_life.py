# https://www.youtube.com/watch?v=fei4bJQdBUQ

class Solution:
    """289. Game of Life"""

    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        # Original | New | State
        #     0    |  0  |   0
        #     1    |  0  |   1
        #     0    |  1  |   2
        #     1    |  1  |   3
        """
        ROWS, COLS = len(board), len(board[0])

        def neighbors(r, c):
            count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or i < 0 or
                        i == ROWS or j < 0 or j == COLS):
                        continue
                    if board[i][j] in [1, 3]:
                        count += 1
            return count


        for r in range(ROWS):
            for c in range(COLS):
                nei = neighbors(r, c)

                if board[r][c]:
                    if nei in [2, 3]:
                        board[r][c] = 3
                elif nei == 3:
                    board[r][c] = 2

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    board[r][c] = 1
        """
        The time complexity is O(n * m) as each cell is visited twice.
        The time complexity is O(1) as no data structures were used.
        """

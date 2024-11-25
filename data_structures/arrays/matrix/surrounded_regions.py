class Solution:
    """130. Surrounded Region"""

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Intuition:
        1. Find the region of each border cell that contains an "O".
        2. Mark those regions in the board with a different letter.
        3. Iterate over the board and capture the remaining "O" cells
           that were not marked, and restore the marked cells to an "O".
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                board[r][c] != "O"):
                return

            # Mark the region of border cell as visited
            board[r][c] = "V"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Mark the region of the border cells
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[-1][c] == "O":
                dfs(ROWS - 1, c)
        for r in range(1, ROWS - 1):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][-1] == "O":
                dfs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "V":
                    board[r][c] = "O"

        """
        The time complexity is O(m * n), where m * n is the size of the
        board. Each cell is visited at most twice.

        The space complexity is O(1), excluding the recursion stack, due
        to board being modified in place to mark visited cells.
        """


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Intuition:
        1. Find all connected non-border cells that contains an "O".
        2. Store the positions of those cells to a list of regions.
        3. Capture each region that is fully surrounded by "X" cells.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        regions = []

        def dfs(r, c, region):
            if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1 or
               (r, c) in region or board[r][c] == "X"):
                return

            region.add((r, c))

            # Mark visited cells in place to save space
            # Change back to "O" later if is not surrounded
            board[r][c] = "X"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, region)

            return region

        def surrounded(region):
            res = True
            for r, c in region:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in regions:
                        continue
                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS or
                        board[nr][nc] != "X"):
                        res = False
                        break
            return res

        for r in range(1, ROWS - 1):  # O(m * n) time and space
            for c in range(1, COLS - 1):
                if board[r][c] == "O":
                    region = dfs(r, c, set())
                    regions.append(region)

        for region in regions:
            if not surrounded(region):
                for r, c in region:
                    board[r][c] = "O"
        """
        The time complexity is O(m * n), where m * n is the size of the
        board. Each cell is visited at most twice.

        The space complexity is O(m * n) due to the recursion stack and
        the region storage.
        """

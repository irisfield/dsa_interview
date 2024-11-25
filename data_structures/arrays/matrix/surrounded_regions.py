class Solution:
    """130. Surrounded Region"""

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

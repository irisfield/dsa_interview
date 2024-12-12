class Solution:
    """174. Dungeon Game"""

    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        """
        Dynamic Programming - Minimum Cost
        1. Iterate the matrix in reverse
        2. For each cell, compute the cost it takes to save the pricess.
           Please note that if the cell is positive, it costs 0 HP.
        4. Modify the matrix in place to save space.
        """
        ROWS, COLS = len(dungeon), len(dungeon[0])

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                down, right = float("-inf"), float("-inf")

                if r + 1 < ROWS:
                    down = dungeon[r][c] + dungeon[r + 1][c]

                if c + 1 < COLS:
                    right = dungeon[r][c] + dungeon[r][c + 1]

                if r + 1 == ROWS and c + 1 == COLS:
                    cost = dungeon[r][c] if dungeon[r][c] < 0 else 0
                elif down >= 0 or right >= 0:
                    cost = 0
                else:
                    cost = max(down, right)

                dungeon[r][c] = cost
        """
        The time complexity is O(m * n) as each cell is visited once.
        The space complexity is O(1) as the cost is stored in place.
        """
        return abs(dungeon[0][0]) + 1

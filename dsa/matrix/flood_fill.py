from collections import deque

class Solution:
    """733. Flood Fill"""

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c):

            original = image[r][c]
            image[r][c] = -1  # mark as visited

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    image[nr][nc] == original and
                    image[nr][nc] != color and
                    image[nr][nc] >= 0):
                    dfs(nr, nc)

            image[r][c] = color

        dfs(sr, sc)
        """
        The time complexity O(m * n) as each cell is visited once.

        The space complexity is O(m * n) due to the recursion stack.
        """
        return image

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        ROWS, COLS = len(image), len(image[0])

        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()

            original = image[r][c]
            image[r][c] = color  # also marks visited cells

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr >= 0 and nr < ROWS and
                    nc >= 0 and nc < COLS and
                    image[nr][nc] == original and
                    image[nr][nc] != color):
                    q.append((nr, nc))
        """
        The time complexity O(m * n) as each cell is visited once.

        The space complexity is O(1) as the image is modified in place.
        """
        return image

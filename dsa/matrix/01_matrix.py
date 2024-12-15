from collections import deque

class Solution:
    """542. 01 Matrix"""

    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        """
        Intuition:
        This is a shortest path problem, and the best approach to solve
        it is using BFS. BFS guarantees that we explore all cells level
        by level, ensuring that each cell's distance is calculated in
        the shortest possible way from the nearest zero.

        Add all the cells with zeros to the queue and set all other
        cells to infinity. Then, go through each cell and update its
        distance by checking its neighbors, ensuring that the shortest
        path to a zero is always found.
        """
        ROWS, COLS = len(mat), len(mat[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c, 0))
                else:
                    mat[r][c] = float("inf")

        while q:
            r, c, dist = q.popleft()

            if dist < mat[r][c]:
                mat[r][c] = dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS:
                    continue
                elif mat[nr][nc] == float("inf"):
                    q.append((nr, nc, dist + 1))

        """
        The time complexity is O(m * n), where m and n are the number of
        rows and columns in the matrix. Each cell is processed once, and
        for each cell, we explore its four neighboring cells.

        The space complexity is O(m * n), as the BFS queue can store up
        to m * n cells in the worst case, and the matrix is also
        modified in place.
        """
        return mat

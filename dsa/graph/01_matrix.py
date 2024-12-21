from collections import deque

class Solution:
    """542. 01 Matrix"""

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Intuition: Instead of starting from each 1 and counting the
        steps to the nearest 0, which seems inefficient, do the
        opposite. Start from each 0 and count how many steps it takes to
        reach each the nearest 1. This way, you perform the BFS from
        0 to 1 instead of from 1 to 0. BFS guarantees that the nearest
        0 will reach 1 first.

        Steps:
        1. Initialize a queue
        2. Iterate through the matrix and if the cell is 1, update the matrix in-place by change it to infinity. Otherwise, append the tuple, (row, col, steps), where steps starts at 0, to the queue.
        3. Perform BFS on the queue, only appending the adjacent cell to the queue if it is equal to -1, and increasing the steps by 1.
        4. Update the matrix in-place if the steps is greater than the cell being visited.
        """
        ROWS, COLS = len(mat), len(mat[0])

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                    mat[r][c] = float("inf")
                else:
                    q.append((r, c, 0))

        while q:
            r, c, steps = q.popleft()
            mat[r][c] = min(mat[r][c], steps)

            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS:
                    continue
                elif mat[nr][nc] == float("inf"):
                    q.append((nr, nc, steps + 1))

        """
        The time complexity is O(m * n), where m and n are the number of
        rows and columns in the matrix. Each cell is processed once, and
        for each cell, we explore its four neighboring cells.

        The space complexity is O(m * n), as the BFS queue can store up
        to m * n cells in the worst case, and the matrix is also
        modified in place.
        """
        return mat

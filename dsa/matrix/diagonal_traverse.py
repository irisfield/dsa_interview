class Solution:
    """498. Diagonal Traverse"""

    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        ROWS, COLS = len(mat), len(mat[0])

        res = []
        up = True
        r, c = 0, 0

        while len(res) != ROWS * COLS:
            res.append(mat[r][c])

            if up:
                if r - 1 >= 0 and c + 1 < COLS:
                    r -= 1
                    c += 1
                else:
                    if c + 1 < COLS:
                        c += 1
                    else:
                        r += 1
                    up = False
            else:
                if c - 1 >= 0 and r + 1 < ROWS:
                    r += 1
                    c -= 1
                else:
                    if r + 1 < ROWS:
                        r += 1
                    else:
                        c += 1
                    up = True

        """
        The time complexity is O(m * n) because each element is
        processed exactly once.

        The space complexity is O(1) because other than list to
        store the results no additional space is used.
        """
        return res

print(Solution().findDiagonalOrder([[2,5],[8,4],[0,-1]]))

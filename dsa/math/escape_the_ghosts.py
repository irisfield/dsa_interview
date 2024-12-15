class Solution:
    """789. Escape The Ghosts"""

    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        # If the ghost is closer to the target, you cannot escape.
        # If you and the ghost arrive at the same time, you cannot escape.

        tx, ty = target
        my_dist = abs(tx) + abs(ty)
        for gx, gy in ghosts:  # time O(n)
            ghost_dist = abs(tx - gx) + abs(ty - gy)
            if ghost_dist <= my_dist:
                return False  # ghost is closer to the target

        """
        The time complexity is O(n) because the algorithm loops through
        all the ghosts to calculate their distance to the target.

        The space complexity is O(1) as no extra space is used other
        than a few variables for calculations.
        """
        return True

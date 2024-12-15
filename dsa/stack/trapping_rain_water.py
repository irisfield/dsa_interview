class Solution:
    """42. Trapping Rain Water"""

    def trap(self, height: list[int]) -> int:

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        water = 0

        while l < r:  # time O(n)
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
        """
        The time complexity is O(n), as the heights are processed once
        with two pointers.

        The space complexity is O(1), as no data structures are used.
        """
        return water

    def trap(self, height: list[int]) -> int:
        import collections
        maxLeft = []
        maxRight = collections.deque()
        m, water = 0, 0

        # maximum left height for every single position
        for n in height:  # time O(n)
            maxLeft.append(m)  # space O(n)
            m = max(m, n)

        m = 0

        # maximum right height for every single position
        for n in height[::-1]: # time O(n)
            maxRight.appendleft(m)
            m = max(m, n)

        # compute the amount of water that can be trapped
        for i in range(len(height)):  # time O(n)
            diff = min(maxLeft[i], maxRight[i]) - height[i]
            water += diff if diff > 0 else 0
        """
        The time complexity is O(n), as the heights are processed
        a constant number of times. Once for maxLeft, once for maxRight,
        and once for the water calculation.

        The space complexity is O(n), as maxLeft and maxRight store
        extra data.
        """
        return water

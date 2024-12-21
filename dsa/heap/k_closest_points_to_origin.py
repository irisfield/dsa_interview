class Solution:
    """973. K Closest Points to Origin"""

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Calculate the Euclidean distance of each point from the origin.
        Use a min-heap to store the points with their distances, as it
        allows efficient extraction of the smallest values. After
        inserting all points into the heap, pop the k smallest elements
        to get the k closest points.
        """
        heap = []
        dist = lambda x, y: math.sqrt(x ** 2 + y ** 2)

        for x, y in points:  # O(n) time
            heap.append([dist(x, y), x, y])  # O(n) space

        heapq.heapify(heap)  # O(n) time

        """
        The time complexity is O(n + k log n) because:
        - O(n) for building the heap (heapify).
        - O(k log n) for popping the k smallest elements from the heap.

        The space complexity is O(n), as the heap stores n elements.
        """
        return [heapq.heappop(heap)[1:] for _ in range(k)]

class Solution:
    """1094. Car Pooling"""

    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])  # O(n log n)

        heap = []  # pair of (end, passengers)
        seated = 0

        for passengers, start, end in trips:  # O(n) time

            while heap and heap[0][0] <= start:
                seated -= heap[0][1]
                heapq.heappop(heap)  # O(log n) time

            seated += passengers

            if seated > capacity:
                return False

            heapq.heappush(heap, (end, passengers))  # O(log n) time

        """
        The time complexity is O(n log n) due to the sorting step and
        heap operations for each trip.

        The space complexity is O(n) due to the storage required for the
        heap/priority queue, which can store up to n trips.
        """
        return True

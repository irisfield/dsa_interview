class TimeMap:
    """981. Time Based Key-Value Store"""

    """
    Set will use key to store a value at timestamp.
    Get will return the value at key and timestamp.

    Timestamps are strictly increasing digits (sorted property)

    Store arguments in a way that makes it easy to do binary search:
    { key : [ (timestamp : value) ] }
    """
    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:  # O(m) space
            self.store[key] = []
        self.store[key].append((timestamp, value))  # O(n) space
        """
        The time complexity is O(1) due to the hash map.

        The space complexity is O(m * n), where m is the number of
        distinct keys and n is the average number of timestamp-value
        pairs per key.
        """


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:  # O(1) time
            return ""

        values = self.store[key]  # O(1) time

        l, r = 0, len(values) - 1
        last = -1

        while l <= r:  # O(log n) time
            mid = l + ((r - l) // 2)

            if timestamp == values[mid][0]:
                return values[mid][1]

            if timestamp < values[mid][0]:
                r = mid - 1
            else:
                last = mid
                l = mid + 1

        """
        The time complexity is O(log n) due to the binary search.

        The space complexity is O(1) as no additional memory is used by
        this function.
        """
        return values[last][1] if last >= 0 else ""

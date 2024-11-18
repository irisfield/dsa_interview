class Solution:
    """692. Top K Frequent Words"""

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = {}

        for word in words:  # O(n) time and space
            count[word] = count.get(word, 0) + 1

        # O(n log n) time, O(n) space
        count = sorted(count.items(), key=lambda x: (-x[1], x[0]))

        res = []
        for i in range(k):  # O(n) time
            res.append(count[i][0])

        """
        The time complexity is O(n log n) because of the sorting.

        The space complexity is O(n) because extra space is utilized for
        the dictionary and sorted array.
        """
        return res

class Solution:
    """692. Top K Frequent Words"""

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = {}

        for word in words:  # O(n) time
            count[word] = count.get(word, 0) + 1  # O(n) space

        # O(n log n) time, O(n) space
        top = sorted(count.items(), key=lambda x: (-x[1], x[0]))

        """
        The time complexity is O(n log n) because it is dominated
        by the sorting step.

        The space complexity is O(n) as extra space is utilized
        for the sorted array.
        """
        return [word for word, _ in top][:k]

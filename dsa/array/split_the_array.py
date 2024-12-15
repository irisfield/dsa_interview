class Solution:
    """3046. Split the Array"""

    def isPossibleToSplit(self, nums: list[int]) -> bool:
        if len(nums) & 1:
            return False

        count = {}

        for n in nums:  # O(n) time
            count[n] = 1 + count.get(n, 0)

        for _, v in count.items():  # O(n) time
            if v > 2:
                return False
        """
        The time complexity is O(n), where n is the length of the list.
        The space complexity is O(n), due to the hash map used to store
        frequencies.
        """
        return True

    def isPossibleToSplit(self, nums: list[int]) -> bool:
        if len(nums) & 1:
            return False

        nums1 = set()
        nums2 = set()

        nums.sort()  # O(n log n) time

        for n in nums:  # O(n) time
            if n not in nums1 and len(nums1) <= len(nums2):
                nums1.add(n)
            elif n not in nums2:
                nums1.add(n)
            else:
                return False

        """
        The time complexity is O(n log n), where n is the length of the
        list, due to the sorting operation. The loop runs in O(n) time.

        The space complexity is O(n), as two sets are used to store
        unique elements.
        """
        return len(nums1) == len(nums2)

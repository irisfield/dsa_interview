class Solution:
    """217. Contains Duplicate"""

    def containsDuplicate(self, nums: list[int]) -> bool:
        count = {}
        for n in nums:  # time O(n)
            count[n] = 1 + count.get(n, 0)  # space O(n)
            if count[n] > 1:
                return True
        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(n), as a hash map is used to store counts.
        """
        return False

    def containsDuplicate2(self, nums: list[int]) -> bool:
        nums.sort()  # timsort -> time O(n log n)
        for i in range(len(nums) - 1):  # time O(n)
            if nums[i] == nums[i + 1]:
                return True
        """
        Time complexity is O(n log n), as the sorting step dominates the overall complexity.
        Space complexity is O(1), as no data structures were utilized, and the sorting is done in-place.
        """
        return False

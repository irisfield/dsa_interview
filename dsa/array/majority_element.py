class Solution:
    """169. Majority Element"""

    def majorityElement2(self, nums: list[int]) -> int:
        count = {}
        res, maxCount = 0, 0
        for n in nums:  # time O(n)
            count[n] = 1 + count.get(n, 0)  # space O(n)
            res = n if count[n] > maxCount else res
            maxCount = max(maxCount, count[n])
        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(n), as a hash map is used to store counts.
        """
        return res

    def majorityElement(self, nums: list[int]) -> int:
        """
        Boyer-Moore Algorithm. Only works because we are guaranteed
        a majority element that appears more than half of the times.

        The main idea behind this algorithm is that if there is
        a majority element (i.e., one that appears more than half of the
        times), it will "survive" as the final candidate after a series
        of comparisons and count adjustments.
        """
        res, count = 0, 0
        for i in range(len(nums)):  # time O(n)
            if count == 0:
                res = nums[i]
            if nums[i] == res:
                count += 1
            else:
                count -= 1
        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return res

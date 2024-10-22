class Solution:
    """169. Majority Element"""
    def majorityElement(self, nums: list[int]) -> int:
        """
        Boyer-Moore Algorithm. Only works because we are guaranteed
        a majority element that appears more than half of the times.
        """
        res, count = 0, 0
        for n in nums:  # time O(n)
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        """
        Time complexity is O(n), as each element is processed once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return res

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

assert Solution().majorityElement([3,2,3]) == 3, f"Majority element should be 3"
assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2, f"Majoriy element should be 2"

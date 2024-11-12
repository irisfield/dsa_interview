class Solution:
    """88. Merge Sorted Array"""

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        m -= 1
        n -= 1

        while l >= 0:
            if m >= 0 and n >= 0:
                if nums1[m] > nums2[n]:
                    nums1[l] = nums1[m]
                    m -= 1
                else:
                    nums1[l] = nums2[n]
                    n -= 1
            elif n >= 0:
                nums1[l] = nums2[n]
                n -= 1
            else:
                nums1[l] = nums1[m]
                m -= 1
            l -= 1

        """
        The time complexity is O(n + n) as each element is processed once.
        The space complexity is O(1) as no additional memory is used.
        """

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index of nums1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:  # O(m) time
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # fill nums1 with leftover nums2 elements
        while n > 0:  # O(n) time
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1

        """
        The time complexity is O(n + n) as each element is processed once.
        The space complexity is O(1) as no additional memory is used.
        """

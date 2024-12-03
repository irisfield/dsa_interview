class Solution:
    """1235. Maximum Profit in Job Scheduling"""

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        """
        0 : (1, 3) = 50
        1 : (2, 3) = 10
        2 : (3, 5) = 40
        3 : (3, 6) = 70

        Goal: Compute profit for all combinations of non-overlapping
        intervals.

        Note: A way to check if two intervals are overlapping is needed.

        Idea: Backtracking. The decision tree makes two choices:
        1. Computes profit NOT including the current job
        2. Computes the profit including the current job

        Optimize this approach with memoization and binary search for
        finding the next non-overlapping index. This requires sorting
        the jobs by start time.
        """
        dp = {}
        jobs = []

        for i in range(len(profit)):  # O(n) time
            triplet = (startTime[i], endTime[i], profit[i])
            jobs.append(triplet)  # O(n) space

        # Sort jobs by their start time
        jobs.sort(key=lambda x: x[0])  # O(n log n) time

        def search(i):  # O(log n)
            """Returns the next non-overlapping index."""
            l, r = i + 1, len(profit) - 1

            while l <= r:
                mid = l + ((r - l) // 2)
                if jobs[mid][0] >= jobs[i][1]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def dfs(i):  # O(n) time
            if i == len(jobs):
                return 0
            if i in dp:
                return dp[i]

            # Profit not including the job
            exclude_job = dfs(i + 1)

            # Profit including job
            j = search(i)  # O(log n) time
            include_job = jobs[i][2] + dfs(j)
            dp[i] = max(exclude_job, include_job)
            return dp[i]

        """
        The time complexity is O(n log n) due to sorting the jobs and
        performing binary search for each job in the dfs function.

        The space complexity is O(n) to store the jobs list, the
        memoization dictionary, and the recursion stack.
        """
        return dfs(0)

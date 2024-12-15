class Solution:
    """39. Combination Sum"""

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        # Decision tree with two dicisions:
        # - include candidate[i]
        # - do not candidate[i]
        def dfs(i, cur, total):  # time O(2^t)
            if total == target:
                res.append(cur.copy())  # append combination
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])  # include candidate[i]
            dfs(i, cur, total + candidates[i])
            cur.pop()  # do not include candidate[i]
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        """
        Time complexity is O(2^t), where t is the target.
        Space complexity is O(t + k), where:
          - t is the maximum depth of recursion
          - k is number of valid combinations
        """
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """102. Binary Tree Level Order Traversal"""

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        # Breadth-first Search
        if not root:
            return []

        from collections import deque
        q = deque([root])
        res = []

        while q:  # O(n) time
            length = len(q)
            level = []
            for _ in range(length):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)  # O(n) space
                if node.right:
                    q.append(node.right)  # O(n) space
            res.append(level)
        """
        The time complexity is O(n), as each node is processed exactly once.
        The space complexity is O(n), as a queue is utilized for the traversal.
        """
        return res

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        # Recursive Depth-first Search: Pre-order Traversal
        if not root:
            return []

        self.res = []
        def dfs(node, i):  # O(n) time
            if not node:
                return None

            if i > len(self.res) - 1:
                self.res.append([node.val])
            else:
                self.res[i].append(node.val)

            dfs(node.left, i + 1)
            dfs(node.right, i + 1)
        dfs(root, 0)
        """
        The time complexity is O(n) as each node is processed exactly once.
        The time complexity is O(n) as the call stack can grow up to n.
        """
        return self.res


    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        # Iterative Depth-first Search: Pre-order Traversal
        if not root:
            return []

        res = []
        stack = [(root, 0)]
        while stack:
            length = len(stack)
            for _ in range(length):
                node, i = stack.pop()

                if i > len(res) - 1:
                    res.append([node.val])
                else:
                    # This require to swap the order due to
                    # the nature of the stacks
                    val = res[i].pop()
                    res[i].append(node.val)
                    res[i].append(val)

                if node.left:
                    stack.append((node.left, i + 1))
                if node.right:
                    stack.append((node.right, i + 1))
        """
        The time complexity is O(n) as each node is processed exactly once.
        The space complexity is O(n), as a stack is utilized for the traversal.
        """
        return res

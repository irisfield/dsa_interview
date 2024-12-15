# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """104. Maximum Depth of Binary Tree"""

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive Depth-first Search
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        """
        The time complexity is O(n), where n is the number of nodes.
        The space complexity is O(n), as the call stack can go up to n.
        """
        return 1 + max(left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative Depth-first Search
        if not root:
            return 0

        stack = [(root, 1)]
        depth = 0

        while stack:
            node, d = stack.pop()
            depth = max(depth, d)
            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))
        """
        The time complexity is O(n), where n is the number of nodes.
        The space complexity is O(n), as the stack can grow up to n.
        """
        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Breadth-first Search
        if not root:
            return 0

        from collections import deque
        q = deque([(root, 1)])
        depth = 0

        while q:
            node, d = q.popleft()
            depth = max(depth, d)
            if node.left:
                q.append((node.left, d + 1))
            if node.right:
                q.append((node.right, d + 1))
        """
        The time complexity is O(n), where n is the number of nodes.
        The space complexity is O(n), as the queue can grow up to n.
        """
        return depth

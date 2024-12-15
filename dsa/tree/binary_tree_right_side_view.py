# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    """199. Binary Tree Right Side View"""

    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        # Breadth-First Search / Level Ordered Traversal
        res = []
        q = deque([root])

        while q:
            right = None

            for _ in range(len(q)):
                node = q.popleft()
                right = node

                # The order is important: left before right
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if right:
                q.append(right.val)

        """
        The time complexity is O(n). Each node is processed exactly once.
        The space complexity is O(w), where w is maximum width of the tree.
        """
        return res


    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            # The order is important: right before left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        """
        The time complexity is O(n). Each node is processed exactly once.
        The space complexity is O(w), where w is maximum width of the tree.
        """
        return res

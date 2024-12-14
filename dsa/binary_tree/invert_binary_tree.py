# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    """226. Invert Binary Tree"""

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        """
        The time complexity of the function is O(n), as each node is
        visited once, and the swap operation takes constant time. The
        time complexity does not depend on whether the tree is balanced
        or not because each node is still visited exactly once.

        The space complexity is O(h), where h is the height of the tree.
        This is because the recursion stack grows with the height of the
        tree. In the worst case (unbalanced tree), the space complexity
        is O(n). In the best case (balanced tree), it is O(log n).
        """
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])

        while q:
            node = q.pop()

            # swap children
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        """
        The time complexity is O(n), where n is the number of nodes in the tree.
        This is because each node is visited once while performing the swap operation.

        The space complexity is O(n). In the worst case, for a balanced
        tree, the queue will store up to n/2 nodes, which is still O(n).
        """
        return root

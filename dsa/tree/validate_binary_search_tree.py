# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """98. Validate Binary Search Tree"""

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition:
        Validate the value of each node against a left and right bound.
        As the tree is traversed recursively, the left and right bounds
        are passed down for each node, ensuring that the node's value
        adheres to the BST properties.
        """
        def dfs(node, left, right):
            if not node:
                return True

            if not (node.val > left and node.val < right):
                return False

            return (dfs(node.left, left, node.val) and
                    dfs(node.right, node.val, right))

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
        return dfs(root, float("-inf"), float("inf"))

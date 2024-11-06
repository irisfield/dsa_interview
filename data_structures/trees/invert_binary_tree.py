# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
        The time complexity is O(n) as the depth of the recursion
        depends on the height of the tree. In the worst case, if the
        tree is completely unbalanced (e.g., a skewed tree), the height
        of the tree could be O(n), where n is the number of nodes.

        The space complexity is O(h), where h is the height of the tree.
        If the tree is balanced then h = O(log n).
        """
        return root

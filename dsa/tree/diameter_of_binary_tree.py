# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """543. Diameters of Binary Tree"""

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):  # O(n) time and space
            nonlocal diameter
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            # diameter = left height + right height
            diameter = max(diameter, left + right)

            # return the max height/depth of the root
            return 1 + max(left, right)

        dfs(root)
        """
        The time complexity is O(n) as each node is visited exactly once.
        The space complexity is O(log n) if the binary tree is balanced.
        The space complexity is O(n) if the binary tree is unbalanced.
        """
        return diameter

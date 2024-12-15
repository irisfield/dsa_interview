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
        The time complexity is O(n), where n is the number of nodes in
        the tree, as each node is visited exactly once.

        The space complexity is O(h), where h is the height of the tree,
        due to the recursion stack.
        """
        return dfs(root, float("-inf"), float("inf"))

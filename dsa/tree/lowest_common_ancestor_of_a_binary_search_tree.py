# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """235. Lowest Common Ancestor of a Binary Search Tree"""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        p and q are guaranteed to exist and all values are unique.
        """

        def dfs(node):
            if not node:
                return None

            if node.val in [p.val, q.val]:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            elif left:
                return left
            else:
                return right

        """
        The time complexity is O(n). In the worst case, every node in
        the tree is visited once, where n is the number of nodes in the
        tree.

        The space complexity is O(n). In the worst case, if the tree is
        unbalanced, the recursion stack will store all the nodes in the
        tree (i.e., the height of the tree). In the best case, for
        a balanced tree, the space complexity is O(log n), where n is
        the number of nodes.
        """
        return dfs(root)

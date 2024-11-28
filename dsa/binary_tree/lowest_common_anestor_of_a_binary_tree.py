# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """236. Lowest Common Ancestor of a Binary Tree"""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

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
            elif right:
                return right
        """
        The time complexity is O(n), where n is the number of nodes.
        The space complexity is O(h), where h is the height of the tree.
        In the case of a balanced tree, h is O(log n).
        """
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """110. Balanced Binary Tree"""

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """"
        Bottom-Up Approach - Post-order Traversal
        Traverse the tree from the leaves (post-order),
        computing the height of the subtrees and checking
        for balance. A tree is balanced if, for every node,
        the height difference between the left and right
        subtrees does not exceed 1.
        """
        if not root:
            return True

        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]
        """
        The time complexity is O(n), where n is the number of nodes.
        The space complexity is O(h), where h is the height of the tree.
        """
        return dfs(root)[0]

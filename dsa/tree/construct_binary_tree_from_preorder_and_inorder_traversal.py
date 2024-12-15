# Definition for a binary tree node.
# from typing import Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """105. Construct Binary Tree from Preorder and Inorder Traversal"""

    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        """
        The time complexity is O(n) as each node is visited once and
        perform operations like index lookup on the inorder list, which
        takes O(n) time for each recursive call.

        The space complexity is O(n), where n is the total number of
        nodes, because of the recursion stack and the space used to
        store the tree.
        """
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """199. Binary Tree Right Side View"""
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        # Breadth-First Search / Level Ordered Traversal
        res = []
        q = collections.deque([root])

        while q:
            length = len(q)

            for i in range(length):
                node = q.popleft()
                if i == (length - 1):
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        """
        The time complexity is O(n). Each node is processed exactly once.
        The space complexity is O(w), where w is maximum width of the tree.
        """
        return res

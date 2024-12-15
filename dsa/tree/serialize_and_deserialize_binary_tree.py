# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:
    """297. Serialize and Deserialize Binary Tree"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = []
        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    res.append("NaN")
                    continue
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

        """
        The time complexity is O(n), where n is the number of nodes in
        the binary tree. The method iterates through all nodes, adding
        them to the result string.

        The space complexity is O(n), as the method uses a queue to
        store nodes at each level of the tree and creates a result list
        that holds n elements.
        """
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()
            if nodes[i] != "NaN":
                node.left = TreeNode(nodes[i])
                q.append(node.left)
            i += 1
            if nodes[i] != "NaN":
                node.right = TreeNode(nodes[i])
                q.append(node.right)
            i += 1

        """
        The time complexity is O(n), where n is the number of nodes in
        the tree. The method processes each node once to reconstruct the
        tree.

        The space complexity is O(n), as the method stores all nodes in
        a queue and uses a list to store the serialized data.
        """
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

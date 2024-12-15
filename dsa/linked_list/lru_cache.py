class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    """146. LRU Cache"""

    def __init__(self, size: int):  # space O(size)
        self.map = {}
        self.size = size
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:  # time O(1)
        if key not in self.map:
            return -1
        node = self.map[key]
        self.removeNode(node)
        self.insertAfterHead(node)
        return node.val

    def put(self, key: int, val: int) -> None:  # time O(1)
        if key in self.map:
            node = self.map[key]
            node.val = val
            self.removeNode(node)
            self.insertAfterHead(node)
        else:
            if len(self.map) == self.size:
                node = self.tail.prev
                self.removeNode(node)
                del self.map[node.key]
            node = Node(key, val)
            self.map[key] = node
            self.insertAfterHead(node)

    def removeNode(self, node: "Node") -> None:  # time O(1)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def insertAfterHead(self, node: Node) -> None:  # time O(1)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def __str__(self):
        res = ""
        cur = self.head
        while cur:
            res += f"{cur.val} "
            cur = cur.next

        cache = "{\n"
        for k, v in self.map.items():
            cache += f"  {k} : Node({v.val})\n"
        cache += "}"

        return f"{res}\n{cache}"

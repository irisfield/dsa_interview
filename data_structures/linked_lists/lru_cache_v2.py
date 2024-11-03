class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    """146. LRU Cache"""

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.removeNode(node)
        self.insertAfterHead(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.removeNode(node)
            self.insertAfterHead(node)
        else:
            if len(self.cache) == self.capacity:
                node = self.tail.prev
                self.removeNode(node)
                del self.cache[node.key]
            node = Node(key, val)
            self.cache[key] = node
            self.insertAfterHead(node)

    def removeNode(self, node: "Node") -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def insertAfterHead(self, node: "Node") -> None:
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
        for k, v in self.cache.items():
            cache += f"  {k} : Node({v.val})\n"
        cache += "}"

        return f"{res}\n{cache}"


# Test
l = LRUCache(2)
l.put(1, 1)
l.put(2, 2)
l.put(3, 3)
l.put(3, 4)

print(l)
print(l.get(1), l.get(4), l.get(3))

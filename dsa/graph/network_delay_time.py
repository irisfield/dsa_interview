class Solution:
    """743. Network Delay Time"""

    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Dijkstra's shortest path algorithm uses a priority queue (or
        a min-heap) to find the shortest path from a starting node to
        all other nodes in a graph. First, convert the graph from
        a matrix (or edge list) representation into an adjacency list
        using a hash map. Then, initialize the priority queue with the
        starting node and its distance (typically 0 for the starting
        node). Next, iteratively perform a relaxation process, where you
        extract the node with the smallest distance from the priority
        queue, update the distances of its neighbors, and add them back
        to the priority queue (using heappush in Python). This continues
        until all nodes are processed or the shortest paths are found.
        """
        path = []
        edges = { u : [] for u in range(1, n + 1) }

        for u, v, w in times:
            edges[u].append((v, w))

        heap = [(0, k)]
        visited = set()
        time = 0

        while heap:
            weight, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)

            time = max(time, weight)

            for nei_node, nei_weight in edges[node]:
                if nei_node in visited:
                    continue
                heapq.heappush(heap, (nei_weight + weight, nei_node))

        """
        The time complexity is O((V + E) log V), where V is the number
        of nodes and E is the number of edges. This arises because each
        node and edge are processed in the graph traversal, and the
        priority queue operations (push and pop) take O(log V) time.

        The space complexity is O(V + E), where V accounts for the
        storage of nodes in the priority queue and the visited set, and
        E accounts for the storage of adjacency lists representing the
        edges.
        """
        return time if len(visited) == n else -1

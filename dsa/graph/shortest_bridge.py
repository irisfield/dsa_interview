class Solution:
    """934. Shortest Bridge"""

    def shortestBridge(self, grid: list[list[int]]) -> int:
        """
        1. First, use DFS to identify the cells of the first island
           (i.e., the first group of connected 1's). Mark all the cells
           of this island as visited.

        2. After identifying the first island, start a BFS from all the
           cells of the first island. The goal of the BFS is to find the
           shortest path to the second island (the closest group of
           connected 1's). During BFS, it explores neighboring cells and
           expand outwards, counting the number of steps taken until we
           encounter a cell of the second island.

        The algorithm efficiently finds the shortest path between the
        two islands by combining DFS to mark the first island and BFS to
        find the shortest path to the second island.

        BFS will always give the shortest path in an unweighted graph.
        If the graph is weighted (i.e., edges have weights), BFS does
        not guarantee the shortest path, because it treats all edges as
        having equal weight. In this case, algorithms like Dijkstra's
        algorithm or Bellman-Ford are more suitable for finding the
        shortest path.

        Complexity: O(n^2), since we use additional space for the
        visited set and the queue in BFS, both of which can store up to
        n^2 cells in the worst case.

        The time complexity is O(n^2), as this a n x n grid and DFS and
        BFS tarverse all the cells exactly once.

        The space complexity is O(n^2), as the set and the queue can
        hold all n^2 cells in the worst case.
        """
        from collections import deque
        N = len(grid)  # this is an n x n grid
        visited = set()

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (r < 0 or c < 0 or r == N or c == N or
                not grid[r][c] or (r, c) in visited):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, deque(visited)
            while q:
                length = len(q)
                for _ in range(length):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr , nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr == N or nc == N or
                            (nr, nc) in visited):
                            continue
                        if grid[nr][nc]:
                            return res
                        q.append((nr, nc))
                        visited.add((nr, nc))
                res += 1

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()

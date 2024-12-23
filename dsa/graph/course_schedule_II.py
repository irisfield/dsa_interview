class Solution:
    """210. Course Schedule II"""

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Topological sort is an algorithm that arranges the vertices of
        a directed graph in a linear order such that, for every directed
        edge u → v, vertex u appears before vertex v in the order.

        It is useful in scenarios where certain tasks must be performed
        before others, such as task scheduling, course prerequisite
        ordering, dependency resolution.

        Build an adjacency list of the prerequisites for each course.
        Then, do topological via DFS on the each course.
        """
        prereqs = { c : [] for c in range(numCourses) }

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        order = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:  # cycle detected
                return False
            if course in visited:
                return True

            cycle.add(course)

            for prereq in prereqs[course]:
                if dfs(prereq) == False:
                    return False

            cycle.remove(course)
            visited.add(course)
            order.append(course)

            return True

        for course in range(numCourses):  # O(n + p) time and space
            if dfs(course) == False:
                return []

        """
        The time complexity is O(n + p), where n is the number of
        courses (nodes) and p is the number of prerequisites (edges).
        The adjacency list construction takes O(n + p), and the DFS
        search also takes O(n + p) time, as each node (course) and edge
        (prerequisite) are processed at most twice.

        The space complexity is O(n + p). The adjacency list requires
        O(n + p) space to store the courses and their prerequisites. The
        visited set requires O(n) space to store the state of each
        course during DFS traversal. Finally, the call stack also
        requires O(n) space as the recursion can grow up to n courses.
        """
        return order

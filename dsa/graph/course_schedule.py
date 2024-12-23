class Solution:
    """207. Course Schedule"""

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Adjacency List
        Make an adjancency list where each course number maps to all of
        its prerequisites.
        """
        prereqs = { c : [] for c in range(numCourses) }  # O(n) time and space

        for course, prereq in prerequisites:  # O(p) time and space
            prereqs[course].append(prereq)

        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if prereqs[course] == []:
                return True

            cycle.add(course)

            for prereq in prereqs[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            prereqs[course] = []
            return True

        for course in range(numCourses):  # O(n + p) time and space
            if not dfs(course):
                return False

        """
        The time complexity is O(n + p), where n is the number of
        courses (nodes) and p is the number of prerequisites (edges).
        The adjacency list construction takes O(n + p), and the DFS
        search also takes O(n + p) time, as each node (course) and edge
        (prerequisite) are processed at most once.

        The space complexity is O(n + p). The adjacency list requires
        O(n + p) space to store the courses and their prerequisites. The
        visited set requires O(n) space to store the state of each
        course during DFS traversal. Finally, the call stack also
        requires O(n) space as the recursion can grow up to n courses.
        """
        return True

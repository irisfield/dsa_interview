# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """141. Linked List Cycle"""
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Floyd's Cycle Detection: Hare-Tortoise Algorithm"""
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next  # move slow pointer by 1
            fast = fast.next.next  # move fast pointer by 2

            if slow == fast:
                return True
        """
        Time complexity is O(n), as the list is traversed once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        seen = set()  # sets are hashed

        while cur:
            if cur in seen:  # O(1)
                return True
            seen.add(cur)
            cur = cur.next
        """
        Time complexity is O(n), as the list is traversed once.
        Space complexity is O(n), as we are using a set to keep track of seen nodes.
        """
        return False

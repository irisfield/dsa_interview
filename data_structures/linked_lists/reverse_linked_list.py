# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """206. Reverse Linked List"""
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        cur = head
        while cur:
            stack.append(cur.val)  # O(n) time, O(n) space
            cur = cur.next

        cur = head
        while stack:  # Pop values to reverse the list
            cur.val = stack.pop()  # O(n) time
            cur = cur.next

        """
        Time complexity is O(n), as the list is traversed exactly twice.
        Space complexity is O(n), as a stack is used to collect the values.
        """
        return head

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """In-Place Reversal"""
        cur = head
        prev = None

        while cur:
            node = cur.next  # store next node
            cur.next = prev  # in-place reversal
            prev = cur  # set previous node
            cur = node  # go to the next node
        """
        Time complexity is O(n), as the list is traversed exactly once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """21. Merge Two Sorted Lists"""

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0)
        cur = dummy

        while l1 and l2:  # time O(n)
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # append the rest of the bigger list to the sorted list
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2

        """
        Time complexity is O(n), as the two lists are merged in a single pass.
        Space complexity is O(1), as no data structures were utilized.
        """
        return dummy.next

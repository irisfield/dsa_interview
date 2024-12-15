# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """876. Middle of the Linked List"""
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Floyd's Cycle Detection: Hare-Tortoise Algorithm"""
        slow = head
        fast = head


        # When the fast pointer reaches the end of the list,
        # the slow pointer will be at the middle.
        while fast and fast.next:  # O(n) time
            slow = slow.next
            fast = fast.next.next

        """
        Time complexity is O(n), as the list is traversed exactly once.
        Space complexity is O(1), as no data structures were utilized.
        """
        return slow

    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        cur = head
        while cur:  # O(n) time
            arr.append(cur)  # O(n) space
            cur = cur.next

        """
        Time complexity is O(n), as the list is traversed exactly once.
        Space complexity is O(n), as an array was used to store the nodes.
        """
        return arr[len(arr) // 2]

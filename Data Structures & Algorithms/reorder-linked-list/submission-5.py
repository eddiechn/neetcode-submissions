# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            curNext = cur.next
            cur.next = prev
            prev = cur
            cur = curNext


        second = prev
        first = head
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
        
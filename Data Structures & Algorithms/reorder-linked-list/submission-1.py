# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        second_half = slow.next
        slow.next = None # seperatomg the two

        prev = None
        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp

        # merge two halves
        second = prev
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

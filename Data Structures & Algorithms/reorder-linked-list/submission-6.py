# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        split the list into two lists
        reverse the second list
        merge two lists



        """

        # split
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        slow.next = None
        prev = None

        while second:
            curNext = second.next
            second.next = prev
            prev = second
            second = curNext


        second = prev
        first = head


        while second:
            t1, t2 = first.next, second.next

            first.next = second
            second.next = t1
            first, second = t1, t2
        

    
        






















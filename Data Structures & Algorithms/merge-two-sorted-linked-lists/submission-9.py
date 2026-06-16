# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        if n1 < n2:
            append n1 to res
            l1 = l1.next

        while l1 and l2:
            ...
        list.next = whichever is left
        
        """
        dummy = head = ListNode(0)

        l1 = list1
        l2 = list2

        while l1 and l2:
            n1 = l1.val
            n2 = l2.val

            if n1 < n2:
                head.next = ListNode(n1)
                l1 = l1.next

            else:
                head.next = ListNode(n2)
                l2 = l2.next

            head = head.next


        if l1:
            head.next = l1

        elif l2:
            head.next = l2


        return dummy.next
                
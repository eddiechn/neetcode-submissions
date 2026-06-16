# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = head = ListNode(0)
        
        while list1 and list2:
            l1 = list1.val
            l2 = list2.val

            if l1 <= l2:
                head.next = ListNode(l1)
                list1 = list1.next
            else:
                head.next = ListNode(l2)
                list2 = list2.next

            head = head.next

        if list1:
            head.next = list1

        if list2:
            head.next = list2


        return dummy.next
        
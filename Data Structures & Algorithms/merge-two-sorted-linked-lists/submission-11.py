# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 and list2:
            l1 = list1.val
            l2 = list2.val
            if l1 <= l2:
                cur.next = ListNode(l1)
                list1 = list1.next
            else:
                cur.next = ListNode(l2)
                list2 = list2.next

            cur = cur.next

        if list1: 
            cur.next = list1
        if list2:
            cur.next = list2


        return dummy.next
                

                

        
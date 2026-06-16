# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not list1: return list2
        if not list2: return list1
        if list1 == [] and list2 == []: return []

        dummy = ListNode(0)
        prev1 = dummy
        curr1 = list1
        curr2 = list2
       

        while curr1 and curr2:
            if curr1.val <= curr2.val: 
                prev1.next = curr1
                curr1 = curr1.next
            else:
                prev1.next = curr2
                curr2 = curr2.next
            prev1 = prev1.next
        prev1.next = curr1 if curr1 else curr2
        return dummy.next
        





        
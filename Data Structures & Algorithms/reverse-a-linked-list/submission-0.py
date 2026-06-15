# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == []: return []

        # 1->2->3->4
        prev = None
        curr = head

        #  <- 1   ->  2  ->  3  ->4
        #      prev           curr  
        #                head
        

        while curr:
            head = curr.next
            curr.next = prev
            prev = curr
            curr = head
        return prev





        
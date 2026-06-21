# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr, prev = slow.next, None
        slow.next = None
        while curr :
            nx= curr.next
            curr.next = prev
            prev = curr
            curr = nx
        p1, p2 = head, prev
        while p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2


        
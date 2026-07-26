# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0,len(lists),2):
                left = lists[i]
                right = lists[i+ 1] if i+1 < len(lists) else None
                merged.append(self.merge(left,right))
            lists = merged
            
        return lists[0]


    def merge(self,left, right):   
        result = ListNode(0)
        pointer = result
        i = j = 0
        while left and right:
            if left.val <= right.val:
                pointer.next = left
                left = left.next
            else:
                
                pointer.next = right
                right = right.next
            pointer = pointer.next
            
        pointer.next = left if left else right

        return result.next

        

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        curr = head
        dicts = {}
        node = Node(curr.val)
        dicts[curr] = node
        curr = curr.next
        rem = node
        while curr:
            new_node = Node(curr.val)
            rem.next = new_node
            dicts[curr] = new_node
            rem = rem.next
            curr = curr.next

        rando = head
        randc = node
        while randc:
            randc.random = dicts.get(rando.random)
            rando = rando.next
            randc = randc.next


        print(node)
            
        

        return node

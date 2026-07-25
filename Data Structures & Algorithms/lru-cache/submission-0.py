class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

        
    def remove(self, node):
        pre, net = node.prev, node.next
        pre.next = net
        net.prev = pre
        return node

    def insert(self, node):
        pre = self.right.prev
        net = self.right

        pre.next = node
        net.prev = node

        node.prev = pre
        node.next = net

    def get(self, key: int) -> int:
        if key in self.cache:
            # update to most use by removing it first and then inserting it again to the right
            node = self.remove(self.cache[key])
            self.insert(node)
            return node.value
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newnode = Node(key,value)
        self.cache[key] = newnode
        self.insert(newnode)
        
        # check if it exceed the capcacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
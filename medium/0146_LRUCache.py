class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  
        
        self.head = Node(0, 0)  # least recently used
        self.tail = Node(0, 0)  # most recently used
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prevNode, nextNode = node.prev, node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def add(self, node): #add to rightmost - most recently used
        prevNode, nextNode = self.tail.prev, self.tail

        self.tail.prev = node
        node.next = self.tail

        prevNode.next = node
        node.prev = prevNode

    def get(self, key: int) -> int: 
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        #case 1
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        #case 2. Once added node, if over capaity, evict.
        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

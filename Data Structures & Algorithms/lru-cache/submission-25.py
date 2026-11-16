class LRUNode:
    def __init__(self, key: int, value: int, prev: Optional["LRUNode"]=None, next: Optional["LRUNode"]=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        # create leafs
        self.left = LRUNode(-1, -1,)
        self.right = LRUNode(-1,-1,)
        # init list
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        node = LRUNode(key, value)
        self.cache[key] = node
        self.insert(node)

    def insert(self, node: LRUNode):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        self.right.prev = node
    
    def remove(self, node: LRUNode):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        

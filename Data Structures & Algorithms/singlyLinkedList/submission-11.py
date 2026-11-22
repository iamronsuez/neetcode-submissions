class Node:
    def __init__(self,  val: Optional[int] = None, right: Optional["Node"] = None):
        self.val = val
        self.right = right
    

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def get(self, index: int) -> int:
        curr, i = self.head.right, 0
        while curr:
            if i == index:
                return curr.val
            curr, i = curr.right, i + 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val=val, right=self.head.right)
        self.head.right = new_node
        if new_node.right is None:
            self.tail = new_node
            
        
    def insertTail(self, val: int) -> None:
        new_node = Node(val=val)
        self.tail.right = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        prev, curr, i = self.head, self.head.right, 0
        while (curr and i != index):
            prev = curr
            curr = curr.right
            i += 1
        
        if curr is None:
            return False

        prev.right = curr.right
        if curr is self.tail:
            self.tail = prev
        return True


    def getValues(self) -> List[int]:
        values = []
        curr = self.head.right
        while (curr):
            values.append(curr.val)
            curr = curr.right
        return values
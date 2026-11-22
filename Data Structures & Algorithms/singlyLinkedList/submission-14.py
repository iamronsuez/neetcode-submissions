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
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.right
        
        # Remove the node ahead of curr
        if curr and curr.right:
            if curr.right == self.tail:
                self.tail = curr
            curr.right = curr.right.right
            return True
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.right
        while (curr):
            values.append(curr.val)
            curr = curr.right
        return values
class Node:
    def __init__(self,  val: Optional[int], right: Optional["Node"]):
        self.val = val
        self.right = right
    

class LinkedList:
    
    def __init__(self):
        self.head = Node(val=None, right=None)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head
        counter = 0
        while (curr.right):
            node = curr.right
            if counter == index:
                return node.val
            counter +=1
            curr = curr.right
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val=val, right=self.head.right)   # ¿a quién apunta el nuevo primero?
        self.head.right = new_node                 # el centinela apunta a...
        if new_node.right is None:            # la lista estaba vacía
            self.tail = new_node
            
        
    def insertTail(self, val: int) -> None:
        new_node = Node(val=val, right=None)
        self.tail.right = new_node    # 1. enlazar
        self.tail = new_node          # 2. avanzar

    def remove(self, index: int) -> bool:
        counter = 0
        prev, curr = self.head, self.head.right
        while (curr and counter != index):
            prev = curr
            curr = curr.right
            counter += 1
        
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
class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None) 
        self.k, self.len = k,0
        self.head.right, self.tail.left = self.tail, self.head

    def insert(self, node: ListNode, new: ListNode): 
        n = node.right 
        node.right = new 
        new.left, new.right = node, n 
        n.left = new  

    def remove(self, node : ListNode):
        n = node.right.right 
        node.right = n
        n.left = node 

    def insertFront(self, value: int) -> bool:
        # Node의 개수가 maximum lengt보다 클 때 false 반환함 
        if self.len == self.k : 
            return False
        self.len += 1 
        self.insert(self.head,ListNode(value))
        return True 

    def insertLast(self, value: int) -> bool:
        if self.len == self.k :
            return False 
        self.len += 1 
        self.insert(self.tail.left,ListNode(value)) 
        return True

    def deleteFront(self) -> bool:
        # 노드가 아무것도 없을 땐 삭제 불가능하니까 False 반환
        if self.len == 0 : 
            return False 
        self.len -= 1 
        self.remove(self.head) #왜냐면 head의 옆에거 삭제해줌 
        return True 

    def deleteLast(self) -> bool:
        if self.len == 0 : 
            return False 
        self.len -= 1 
        self.remove(self.tail.left.left)
        return True 

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1 

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1 

    def isEmpty(self) -> bool:
        return self.len == 0 

    def isFull(self) -> bool:
        return self.len == self.k
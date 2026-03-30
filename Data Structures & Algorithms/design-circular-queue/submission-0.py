class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node(0)
        self.tail = Node(0, self.head, self.head)
        self.head.left = self.tail
        self.head.right = self.tail
        self.capacity = k
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        prev = self.tail.left
        node = Node(value, prev, self.tail)
        prev.right = node
        self.tail.left = node
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        next = self.head.right
        self.head.right = next.right
        next.right.left = self.head
        next.left = next.right = None
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.right.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.left.val

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
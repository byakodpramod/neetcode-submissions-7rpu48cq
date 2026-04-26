class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class MyHashSet:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.store = {}

    def add(self, key: int) -> None:
        nextNode = self.head.next
        newNode = Node(key)
        newNode.next = nextNode
        nextNode.prev = newNode
        newNode.prev = self.head
        self.head.next = newNode
        self.store[key] = newNode

    def remove(self, key: int) -> None:
        if key not in self.store:
            return
        node = self.store[key]
        prevNode, nextNode = node.prev, node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.next = node.prev = None
        self.store.pop(key)

    def contains(self, key: int) -> bool:
        return key in self.store


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
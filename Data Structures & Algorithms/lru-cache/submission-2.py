class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.store = {}
        self.tail = Node(None, None)
        self.front = Node(None, None)
        self.tail.next = self.front
        self.front.prev = self.tail
        self.capacity = capacity

    def __insert__(self, newNode):
        pre = self.front.prev
        newNode.next = self.front
        self.front.prev = newNode
        newNode.prev = pre
        pre.next = newNode
        
    def __remove__(self, node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre
        node.next, node.prev = None, None

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        node = self.store[key]
        self.__remove__(node)
        self.__insert__(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.__remove__(self.store[key])
        newNode = Node(key, value)
        self.__insert__(newNode)
        self.store[key] = newNode
        if len(self.store) > self.capacity:
            toRemove = self.tail.next
            self.__remove__(toRemove)
            del self.store[toRemove.key]
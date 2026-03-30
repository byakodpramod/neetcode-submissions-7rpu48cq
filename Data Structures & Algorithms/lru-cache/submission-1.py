class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node(None,None)
        self.tail=Node(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.offset={}
    
    def __remove__(self,node):
        nextNode = node.next
        prevNode = node.prev
        nextNode.prev = prevNode
        prevNode.next = nextNode
        node.next = node.prev = None
        return node.key

    def __add__(self,node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key in self.offset:
            node = self.offset[key]
            self.__remove__(node)
            self.__add__(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.offset:
            self.__remove__(self.offset[key])
        node = Node(key, value)
        self.__add__(node)
        self.offset[key] = node
        if len(self.offset) > self.capacity:
            toRemove = self.head.next
            key = self.__remove__(toRemove)
            del self.offset[key]
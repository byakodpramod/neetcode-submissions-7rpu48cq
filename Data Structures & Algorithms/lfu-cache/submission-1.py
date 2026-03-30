class Node():
    def __init__(self,key,next=None,prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.store = {}

    def __length__(self):
        return len(self.store)
    
    def __delete__(self,k):
        if k in self.store:
            node = self.store[k]
            nextNode, prevNode = node.next, node.prev
            prevNode.next = nextNode
            nextNode.prev = prevNode
            node.next, node.prev = None, None
            self.store.pop(k)
    
    def __insert__(self,k):
        node = Node(k)
        self.store[node.key] = node
        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node

    def update(self,k):
        self.__delete__(k)
        self.__insert__(k)
    
    def deleteFromHead(self):
        deletedKey = self.head.next.key
        self.__delete__(deletedKey)
        return deletedKey

class LFUCache:

    def __init__(self, capacity: int):
        self.lfuCnt = 0
        self.capacity = capacity
        self.listMap = defaultdict(LRUCache)
        self.keyCnt = defaultdict(int)
        self.valMap = {}

    def counter(self, k):
        cnt = self.keyCnt[k]
        self.keyCnt[k] += 1
        self.listMap[cnt].__delete__(k)
        self.listMap[cnt+1].__insert__(k)
        if cnt == self.lfuCnt and self.listMap[cnt].__length__() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if len(self.valMap) == self.capacity:
            keyToDelete = self.listMap[self.lfuCnt].deleteFromHead()
            self.valMap.pop(keyToDelete)
            self.keyCnt.pop(keyToDelete)
        self.valMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.keyCnt[key])        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
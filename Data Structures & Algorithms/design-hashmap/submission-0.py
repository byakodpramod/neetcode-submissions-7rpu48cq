class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashes = [Node() for _ in range(1000)]        

    def put(self, key: int, value: int) -> None:
        hashVal = key % 1000
        head = self.hashes[hashVal]
        while head.next:
            head = head.next
            if head.key == key:
                head.val = value
                return 
        head.next = Node(key, value)

    def get(self, key: int) -> int:
        hashVal = key % 1000
        head = self.hashes[hashVal]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        hashVal = key % 1000
        head = self.hashes[hashVal]
        prev = head
        while head:
            if head.key == key:
                prev.next = head.next
                head.next = None
                return
            prev = head
            head = head.next
        return
            


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
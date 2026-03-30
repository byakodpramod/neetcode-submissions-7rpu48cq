# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, None)
        dummy.next = head
        l, r = dummy, dummy
        prevPart = l
        while left:
            if left == 1:
                prevPart = l
            l = l.next
            left-=1
        while right:
            r = r.next
            right-=1
        nextPart = r.next
        # print(l.val, r.val, prevPart.val, nextPart.val)
        r.next = None
        prevPart.next = None
        prev = None
        cur = l
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # print(cur.val)
        prevPart.next = prev
        l.next = nextPart
        return dummy.next
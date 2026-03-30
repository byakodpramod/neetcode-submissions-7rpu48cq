# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0,head)
        start,end=dummy,dummy
        while n:
            end = end.next
            n-=1
        while end and end.next:
            start = start.next
            end = end.next
        temp = start.next
        start.next = start.next.next
        temp.next = None
        return dummy.next
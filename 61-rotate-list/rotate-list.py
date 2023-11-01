# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        counter = 1
        while cur.next:
            counter += 1
            cur = cur.next
        cur.next = head
        k = counter - (k % counter)
        cur = head
        first = cur
        for _ in range(1,k):
            cur = cur.next

        first = cur.next
        cur.next = None
        return first
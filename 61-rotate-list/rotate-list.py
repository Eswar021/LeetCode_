# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        a=head
        len=0
        while a:
            a=a.next
            len+=1
        if len <= k:
            for i in range(k%len):
                cur=head
                while cur.next.next:
                    cur=cur.next
                next=cur.next
                cur.next=None
                next.next=head
                head=next
        else:
            for i in range(k):
                cur=head
                while cur.next.next:
                    cur=cur.next
                next=cur.next
                cur.next=None
                next.next=head
                head=next
        return head



        
        
        
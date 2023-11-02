# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash=set()
        cur=head
        pre=None
        if not cur:
            return head
        while cur:
            if cur.val not in hash:
                hash.add(cur.val)
                pre=cur
                cur=cur.next
            else:
                pre.next=cur.next
                cur.next=None
                cur=pre.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from math import gcd
        cur=head
        if not cur.next or not cur:
            return head
        while cur.next:
            temp=cur.next
            cur.next=ListNode(gcd(cur.val, temp.val),temp)
            cur=temp
            temp=temp.next
        return head
        
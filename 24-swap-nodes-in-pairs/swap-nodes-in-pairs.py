# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        count=1
        try:
            while dummy!=None:
                val = dummy.val
                dummy.val=dummy.next.val
                dummy.next.val=val
                dummy=dummy.next.next
        except:
            pass
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        a=[]
        for ll in lists:
            while ll is not None:
                a.append(ll.val)
                ll=ll.next
        cur=dummy=ListNode()
        a.sort()
        for j in a:
            cur.next=ListNode(j)
            cur=cur.next
        return dummy.next

        
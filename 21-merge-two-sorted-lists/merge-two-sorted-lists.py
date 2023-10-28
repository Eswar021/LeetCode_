# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        L=[]
        while list1 is not None:
            L.append(list1.val)
            list1=list1.next
        while list2 is not None:
            L.append(list2.val)
            list2=list2.next
        L.sort()
        dummy=ListNode()
        head=dummy
        for i in L:
            dummy.next=ListNode(i)
            dummy=dummy.next
        return head.next
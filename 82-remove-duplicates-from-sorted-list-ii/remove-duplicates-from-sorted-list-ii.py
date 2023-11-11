# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake=ListNode(0,head)
        pre=fake
        cur=head
        if not head:
            return head
        # while head:
        #     if head.next and head.val==head.next.val:
        #         while head.next and head.val==head.next.val:
        #             head=head.next
        #         pre.next=head.next
        #     else:
        #         pre=pre.next
        #     head=head.next
        while cur:
            while cur.next and cur.val==cur.next.val:
                cur=cur.next
            if pre.next==cur:
                pre=pre.next
                cur=cur.next
            else:
                pre.next=cur.next
                cur=pre.next
                
        return fake.next
            
        # return fake.next
        


        
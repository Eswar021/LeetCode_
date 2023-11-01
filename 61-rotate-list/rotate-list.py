# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len=0
        a=head
        while a:
            a=a.next
            len+=1
        if len<=k and len!=0:
            n=k%len
            for i in range(n):
                curr=head
                while curr.next.next:
                    curr=curr.next
                temp=curr.next
                curr.next=None
                temp.next=head
                head=temp
        
        elif len!=0:
            for i in range(k):
                curr=head
                # if len!=0:
                while curr.next.next:
                    curr=curr.next
                temp=curr.next
                curr.next=None
                temp.next=head
                head=temp
        return head
        # for i in range(n):
        #     curr=head
        #     try:
        #         while curr.next.next:
        #             curr=curr.next
        #         temp=curr.next
        #         curr.next=None
        #         temp.next=head
        #         head=temp
        #     except:
        #         pass
       



        
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        else:
            count=0
            temp=head
            while temp is not None:
                count+=1
                temp=temp.next
            m=count-n
            new=ListNode()
            newhead=new
            print("head ",head )
            for i in range(m):
                new.next=head
                head=head.next
                new=new.next
            new.next=head.next
        return newhead.next           
            
            

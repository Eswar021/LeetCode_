# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # a=[]
        # b=[]
        # temp_node1=l1
        # temp_node2=l2
        # while temp_node1 is not None:
        #     a.append(temp_node1.val)
        #     temp_node1=temp_node1.next
        # while temp_node2 is not None:
        #     b.append(temp_node2.val)
        #     temp_node2=temp_node2.next
        # a.reverse()
        # b.reverse()
        # a=list(map(str,a))
        # b=list(map(str,b))
        # res=int("".join(a))+int("".join(b))
        # res=list(str(res))
        # res.reverse()
        # res=list(map(int,res))
        # head=ListNode()
        # current=head
        # for i in res:
        #     current.next=ListNode(i)
        #     current=current.next
        # return head.next

        head=ListNode()
        current=head
        tot=0
        car=0
        while l1!=None or l2!=None or car>0:
            tot=(l1.val if l1 else 0)+(l2.val if l2 else 0)+car
            car=tot//10
            current.next=ListNode(tot%10)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            current=current.next
        return head.next





        
        
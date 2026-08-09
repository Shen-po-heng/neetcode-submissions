# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tmp1=l1
        tmp2=l2

        while tmp1 and tmp2 :
            tmp1.val=tmp1.val+tmp2.val
            if tmp1.val >= 10:
                tmp1.val=tmp1.val-10
                if tmp1.next == None:
                    tmp1.next = ListNode(1)
                else:
                    tmp1.next.val+=1
            if tmp1.next == None and tmp2.next:
                tmp1.next=tmp2.next
                break
            tmp1=tmp1.next
            tmp2=tmp2.next
        if tmp1:
            print(tmp1.val)
        while tmp1:
            if tmp1.val>=10:
                tmp1.val-=10
                if tmp1.next == None:
                    tmp1.next = ListNode(1)
                else:
                    tmp1.next.val+=1    
            tmp1=tmp1.next
        return l1
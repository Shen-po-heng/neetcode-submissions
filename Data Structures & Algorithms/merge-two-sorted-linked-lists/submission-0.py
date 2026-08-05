# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        tmp1=list1
        tmp2=list2

        while tmp1 != None or tmp2 != None:
            if tmp1 == None:
                current.next=tmp2
                break
            elif tmp2 == None:
                current.next=tmp1
                break
            elif tmp1.val <= tmp2.val:
                current.next = tmp1
                tmp1=tmp1.next
            else:
                current.next = tmp2
                tmp2=tmp2.next
            current = current.next
            
        return dummy.next
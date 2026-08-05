# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_list_head = None
        tmp = head
        while tmp != None:
            if reversed_list_head == None:
                reversed_list_head = tmp
                tmp=tmp.next
                reversed_list_head.next=None
                continue
            tmp_reversed = reversed_list_head
            reversed_list_head = tmp
            tmp = tmp.next
            reversed_list_head.next = tmp_reversed 
        return reversed_list_head
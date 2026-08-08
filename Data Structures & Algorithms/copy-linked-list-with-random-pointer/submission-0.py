"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        tmp=head
        dummy=Node(0)
        copy_tmp=dummy
        old_to_new_table={}

        while tmp:
            copy_tmp.next=Node(tmp.val)
            copy_tmp=copy_tmp.next
            # build responding table
            old_to_new_table[tmp]=copy_tmp
            tmp=tmp.next

        tmp=head
        copy_tmp=dummy.next

        while tmp:
            if tmp.random == None:
                copy_tmp.random = None
            else:
                copy_tmp.random=old_to_new_table[tmp.random]
            copy_tmp=copy_tmp.next
            tmp=tmp.next

        return dummy.next
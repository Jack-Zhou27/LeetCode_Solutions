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
       
        #interweaving nodes solution...

        #first pass: create a copy:
        # 1 -> 2 -> 3 
        # 1 -> 1' -> 2 -> 2' -> 3 -> 3'

        if not head:
            return None
        
        curr = head
        while curr:
            curr_next = curr.next           #create cpy of next node
            copy = Node(curr.val, curr_next)#cpy node

            curr.next = copy                #make curr's next cpy
            curr = curr_next                #update curr to be its original next node

        #second pass: connect the random ptrs
        # 1 -> 1' -> 2 -> 2' -> 3 -> 3' has random ptrs connected now for the original and 's

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            
            curr = curr.next.next

        #third pass: seperate into
        # 1 -> 2 -> 3
        # 1' -> 2' -> 3'

        old_head = head
        cpy_head = head.next
        
        old_curr = old_head
        new_curr = cpy_head

        while old_curr:
            old_curr.next = old_curr.next.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
            else:
                new_curr.next = None
            
            old_curr = old_curr.next
            new_curr = new_curr.next

        return cpy_head




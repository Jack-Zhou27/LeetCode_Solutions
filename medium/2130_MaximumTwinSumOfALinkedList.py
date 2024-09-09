# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        #Use slow and fast pointers to find the middle value of the Linked List
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #Reverse first half of the LinkedList
        prev = None
        current = head
        while current != slow:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        #Move from the middle of the array towards both ends of the array to get the pairs.
        #Note since we have reversed the first half of the LinkedList, we can traverse it
        #as normal
        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res

            



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        #find sorted array
        nums = []
        for listt in lists:
            head = listt
            while head:
                nums.append(head.val)
                head = head.next
        
        nums.sort()

        #convert sorted array into linkedlist
        dummy = ListNode(0)
        head = dummy
        i = 0
        while i < len(nums):
            head.next = ListNode(nums[i])
            head = head.next
            i += 1
        return dummy.next

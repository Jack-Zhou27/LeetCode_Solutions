# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #build the strs
        curr1 = l1
        str1 = []
        curr2 = l2
        str2 = []
        while curr1 or curr2:
            if curr1:
                str1.append(curr1.val)
                curr1 = curr1.next
            if curr2:
                str2.append(curr2.val)
                curr2 = curr2.next
        
        #swap the first and last until str is reversed
        n1 = len(str1)
        for i in range(len(str1) // 2):
            str1[i], str1[n1 - i - 1] = str1[n1 - i - 1], str1[i]

        n2 = len(str2)
        for i in range(len(str2) // 2):
            str2[i], str2[n2 - i - 1] = str2[n2 - i - 1], str2[i]
    
        #turn into str then int to sum
        int1 = int("".join(map(str, str1)) or "0")
        int2 = int("".join(map(str, str2)) or "0")

        temp_ans = int1 + int2

        if temp_ans == 0:
            return ListNode(0)

        #reverse the int
        dummy = ListNode(0)
        curr = dummy
        while temp_ans > 0:
            curr.next = ListNode(temp_ans % 10)
            curr = curr.next
            temp_ans //= 10
        
        return dummy.next

        #practice reversing a linkedlist

        # head = dummy.next
        # prev = None
        # while head:
        #     nextt = head.next
        #     head.next = prev
        #     prev = head
        #     head = nextt

        # return prev


        

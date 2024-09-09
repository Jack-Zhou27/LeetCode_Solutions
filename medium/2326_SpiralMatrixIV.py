# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for i in range(n)] for j in range(m)]
        r = 0
        c = 0
        layer = 0
        first = True
        second = False
        third = False
        fourth = False
        while head:
            matrix[r][c] = head.val
            head = head.next

            #left to right
            if first:
                c += 1
                if c > n - 1 - layer:
                    c = n - 1 - layer
                    first = False
                    second = True
                    r += 1
            
            #top to bottom
            elif second:
                r += 1
                if r > m - 1 - layer:
                    r = m - 1 - layer
                    second = False
                    third = True
                    c -= 1
            
            #right to left
            elif third:
                c -= 1
                if c < layer:
                    c = layer
                    third = False
                    fourth = True
                    r -= 1
            
            #bottom to top
            elif fourth:
                r -= 1
                if r <= layer:
                    fourth = False
                    first = True
                    layer += 1
                    r = layer
                    c = layer

            
        return matrix

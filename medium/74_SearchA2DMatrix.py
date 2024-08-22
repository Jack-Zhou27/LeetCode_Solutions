class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #binary search for the row that the target exists on
        def findRow():
            l = 0
            r = len(matrix) - 1
            while l <= r:
                m = (l + r) // 2
                if matrix[m][0] <= target <= matrix[m][len(matrix[0]) - 1]:
                    return m
                elif target < matrix[m][0]:
                    r = m - 1
                else:
                    l = m + 1

            return -1

        #binary search the row for the solution
        i = findRow()
        if i == -1:
            return False

        l = 0
        r = len(matrix[0]) - 1
        
        while l <= r:
            m = (l + r) // 2
            if target < matrix[i][m]:
                r = m - 1
            elif target > matrix[i][m]:
                l = m + 1
            else:
                return True
        
        return False

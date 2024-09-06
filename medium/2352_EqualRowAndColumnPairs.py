class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashMap = {}
        ans = 0

        #Populate a hashMap where the keys are the rows of the grid. Note that for this to work, the key needs to be of type tuple. 
        for rows in grid:
            key = tuple(rows)
            if key in hashMap:
                hashMap[key] += 1
            else:
                hashMap[key] = 1
        
        #Check for each col of the array if the same row exists. 
        for cols in (zip(*grid)):
            key = tuple(cols)
            if key in hashMap:
                ans += hashMap.get(key)

        return ans

        """
        Slow solution that doesn't use hashing but brute force:

        def isEqual(arr1, arr2):
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True

        ans = 0
        for i in range(len(grid)):
            arr1 = []
            for j in range(len(grid[0])):
                arr1.append(grid[i][j])
            
            for j in range(len(grid)):
                arr2 = []
                for k in range(len(grid[0])):
                    arr2.append(grid[k][j])
                if isEqual(arr1, arr2):
                    ans += 1
        return ans
        """

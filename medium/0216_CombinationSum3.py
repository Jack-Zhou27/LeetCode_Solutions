class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(i, currSum):
            if currSum == n and len(res) == k:
                ans.append(res.copy())
                return 
            elif currSum > n or len(res) >= k:
                return 
            
            for j in range(i, 10):
                res.append(j)
                backtrack(j + 1, currSum + j)
                res.pop(-1)
            
        ans = []
        res = []
        backtrack(1, 0)
        return ans
                

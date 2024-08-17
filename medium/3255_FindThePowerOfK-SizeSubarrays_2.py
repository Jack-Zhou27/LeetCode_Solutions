class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        #sliding window solution 
        ans = [-1 for _ in range(len(nums) - k + 1)]
        
        if k == 1:
            for i in range(len(nums)):
                ans[i] = nums[i]
            return ans
        
        i = 0
        canDo = False
        while i < len(nums) - k + 1:
            if canDo == False:
                j = 1
                while j < k:
                    if nums[i + j] == nums[i + j - 1] + 1:
                        j += 1
                    else:
                        i += j
                        break
                    if j == k:
                        canDo = True
                        ans[i] = nums[i + j - 1]
                        i += 1
            else:
                if nums[i + k - 1] == nums[i + k - 2] + 1:
                    ans[i] = nums[i + k - 1]
                    i += 1
                else:
                    canDo = False
        return ans
                    
                
            
                    
            
        """
        This answer below is TOO slow!!!
        
        ans = []
        for i in range (len(nums) - k + 1):
            tempArray = []
            tempArray.append(nums[i])
            j = 1
            while j < k and nums[i + j] == nums[i + j - 1] + 1:
                tempArray.append(nums[i + j])
                j += 1
            if len(tempArray) == k:
                ans.append(tempArray[len(tempArray) - 1])
            else:
                ans.append(-1)
        return ans
        """

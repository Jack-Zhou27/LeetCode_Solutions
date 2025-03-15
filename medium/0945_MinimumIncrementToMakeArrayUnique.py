class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        for i in range(1, len(nums)):
            if(nums[i] <= nums[i - 1]):
                temp = abs(nums[i] - nums[i - 1]) + 1
                count += temp
                nums[i] = nums[i] + temp
        return count
    


"""
        Doing the question without sorting (like the solution below) will be too slow!!!


        
        hashMap = {}

        def nextCount(target, hashMap):      
            count = 0
            while(target + count in hashMap):
                count += 1
            
            return count


        count = 0
        for item in nums:
            if item not in hashMap:
                hashMap[item] = 1
            else:
                temp = nextCount(item, hashMap)
                hashMap[item + temp] = 1
                count += abs(temp)
                
        
        return count
"""

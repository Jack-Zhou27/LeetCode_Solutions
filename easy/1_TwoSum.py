class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):

            # we do a clever trick to overcome the fact a hashmap can only have one distinct key (if the target is composed of target/2 + target/2)
            complement = target - nums[i]

            #first check if the complement exists as a key in the hashmap. If it does exist, we found our answer
            if complement in numMap:
                ans = [i, numMap[complement]] #return the index, which is the value of our key
                return ans
            numMap[nums[i]] = i #store each number as a key, with its value being its index
        return [] #if we didn't find a valid two sum, return an empty list

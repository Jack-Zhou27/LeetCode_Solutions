class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        uniquetarget = set()
        unique = set()

        ans = []
        for i in range(0, len(nums) - 2): #fix an int to get a two sum problem

            #this is an optional slight optimization. We can skip the calculation if we have seen the same target before
            target = 0 - nums[i]
            if(target in uniquetarget):
                continue
            uniquetarget.add(target)

            #using two pointers to solve the Two Sum questions
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                if(nums[left] + nums[right] < target):
                    left += 1
                elif(nums[left] + nums[right] > target):
                    right -= 1
                else: #this just makes sure that we return unique answers only
                    thisTuple = (nums[i], nums[left], nums[right])
                    if (thisTuple not in unique):
                        ans.append([nums[i], nums[left],nums[right]])
                        unique.add(thisTuple)
                    left += 1
                    
        return ans



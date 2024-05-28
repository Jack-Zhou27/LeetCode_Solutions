class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #build up the multiples from the left side (kind of like prefix sums)
        left = []
        left.append(1)
        for i in range(0, len(nums)):
            left.append(left[i] * nums[i])

        #build up the multiples from the right side
        right = [1] * (len(nums) + 1) #this declares an array of length nums+1 and fills it with the number 1
        for i in range(len(nums) - 1, -1, -1):
            right[i] = right[i + 1] * nums[i] #notice here we built our array from the back to the front

        #print the ans, which is the product of the multiples on the left and on the right
        ans = []
        for i in range(len(nums)):
            ans.append(left[i] * right[i + 1])
        return ans

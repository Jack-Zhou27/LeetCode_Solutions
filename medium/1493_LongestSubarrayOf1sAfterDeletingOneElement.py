class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #find location of all zeros
        zeros = []
        zeros.append(-1) #assuming the starting zero is at index -1 instead of index 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
        
        #edge case
        if len(zeros) == 1 or len(zeros) == 2:
            return len(nums) - 1

        #simulate deleting one zero and finding the length of 1s. We subtract 2 to account for the two zeros we are overcounting in doing so (zero at the start and zero at the middle)
        ans = 0
        for i in range(2, len(zeros)):
            ans = max(ans, zeros[i] - zeros[i - 2] - 2)
        return max(ans, len(nums) - zeros[len(zeros) - 2] - 2)

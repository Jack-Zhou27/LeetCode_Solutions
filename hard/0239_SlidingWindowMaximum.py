class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []
        dq = collections.deque()
        for i in range(len(nums)):
            
            #pop smaller numbers
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            
            dq.append(i) #index based

            #pop outofbounds
            if dq[0] < i - k + 1:
                dq.popleft()
            
            #append ans if full window exists
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans

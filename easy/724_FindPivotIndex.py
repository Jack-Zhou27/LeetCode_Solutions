class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        #establish prefixSum
        prefixSum = []
        prefixSum.append(0)
        for i in nums:
            prefixSum.append(i + prefixSum[-1])

        #calculate pivotIndex
        for j in range(len(prefixSum) - 1):
            if prefixSum[j] == prefixSum[-1] - prefixSum[j + 1]:
                return j
        return -1

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans = []

        temp1 = []
        for i in nums1:
            if i not in nums2:
                temp1.append(i)
        
        temp2 = []
        for i in nums2:
            if i not in nums1:
                temp2.append(i)
        
        ans.append(temp1)
        ans.append(temp2)
        return ans

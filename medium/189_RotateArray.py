class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [n for n in nums] #make a copy of the array
        for i in range(0, len(nums)):

            #handle if your rotations go out of bounds
            if(i + k >= len(nums)):
                n = 1
                while(i + k - n * len(nums) >= len(nums)):
                    n += 1
                nums[i + k - n * len(nums)] = temp[i]
            
            #if rotation is in bound
            else:
                nums[i + k] = temp[i]

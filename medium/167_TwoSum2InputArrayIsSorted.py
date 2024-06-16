class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers
        left = 0
        right = 1

        #keep searching if our target is not found
        while(numbers[left] + numbers[right] != target):
            #Increment right pointer
            if(numbers[left] + numbers[right] < target and right < len(numbers) - 1):
                right += 1
            
            #Increment left pointer
            else:
                #Tricky part: to correct for the fact we may have incremented our right pointer too far,
                #we need to decrement it by doing the following while loop:
                while (numbers[left + 1] + numbers[right] > target):
                    right -= 1
                left += 1
                
        return [left + 1, right + 1]

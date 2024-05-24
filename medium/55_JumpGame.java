class Solution {
    public boolean canJump(int[] nums) {
        int currJump = nums[0];
        if(0 == nums.length - 1) //handle edge cases
            return true;
        if(currJump == 0)  //handle edge cases
            return false;

        int temp = 1;
        for(int i = 1; i < nums.length; i++)
        {
             if(i == nums.length - 1)  //we reached the end of the array so return true
                return true;
                
            if(currJump == 0 || (nums[i] <= 0 && currJump - temp <= 0)) //if we are stuck, return false
                return false;

            if(nums[i] > currJump - temp) //greedily update your jump to the current biggest jump possible
            {
                currJump = nums[i];
                temp = 1;
            }
            else //if the previous jump was the biggest jump, as we move forward in the array, our jump distance decreases
                temp++;
        }
        return true;
    }
}

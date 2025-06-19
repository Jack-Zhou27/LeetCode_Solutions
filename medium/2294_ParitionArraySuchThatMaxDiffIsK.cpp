class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());

        int i = 0; 
        int ans = 1;
        int curr = nums[i];
        while(i < nums.size()){
            if(nums[i] > curr + k){
                ans += 1;
                curr = nums[i];
            }
            i += 1;
        }
        return ans;
    }
}

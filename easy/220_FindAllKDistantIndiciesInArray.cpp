class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == key){
                int j = max(0, i - k);
                if (!ans.empty()) {
                    j = max(j, ans.back() + 1); //+1 to avoid duplicates
                }
                while(j < min((int)nums.size(), i + k + 1)){
                    ans.push_back(j);
                    j += 1;
                }
            }
        }
        return ans;
    }
};

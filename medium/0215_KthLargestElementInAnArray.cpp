class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        for(int i = 0; i < nums.size(); i++){
            minHeap.push(nums[i]);

            //TRICK: if our minHeap > k, we start popping all smallest items we
            //have seen so far k-1 times. 
            if(minHeap.size() > k){
                minHeap.pop();
            }
        }
        //popped k-1 smaller items, we are left with the kth largest. 
        return minHeap.top();
        
    }
};

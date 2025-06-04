class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        //[1,2], [1,3], [2,3], [3,4] has to sort by 2nd elem then 1st elem

        //sort the intervals by their endpt.
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b){
            if (a[1] == b[1]){
                return a[0] < b[0];
            }
            return a[1] < b[1];
        });
        

        //algo
        int ans = 0;
        int indx = 0;
        while(indx < intervals.size()){
            int curr_endpt = intervals[indx][1];
            indx += 1;
            while(indx < intervals.size() && curr_endpt > intervals[indx][0]){
                ans += 1;
                indx += 1;
            }
        }
        return ans;
    }
};

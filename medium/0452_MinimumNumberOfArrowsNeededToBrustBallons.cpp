class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        //sort 
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });

        //algo
        int indx = 0;
        int ans = 0;
        while(indx < points.size()){
            int curr_end = points[indx][1];
            indx += 1;
            ans += 1;
            while(indx < points.size() && points[indx][0] <= curr_end){
                indx += 1;
            }
        }
        return ans; 
    }
};

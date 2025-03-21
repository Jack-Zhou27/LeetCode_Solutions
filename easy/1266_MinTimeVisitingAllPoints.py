class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        #init
        ans = 0
        n = len(points)
        #base case:
        if n == 1:
            return ans
        
        #algo
        for i in range(1, n):
            prev_pt = points[i - 1]
            prev_x = prev_pt[0]
            prev_y = prev_pt[1]

            pt = points[i]
            pt_x = pt[0]
            pt_y = pt[1]

            dist_x = abs(pt_x - prev_x)
            dist_y = abs(pt_y - prev_y)

            diagonal = min(dist_x, dist_y)
            straight = max(dist_x, dist_y) - diagonal

            ans += diagonal + straight 

        return ans

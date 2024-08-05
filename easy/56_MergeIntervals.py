class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #sort the 2D array by the 0th collumn
        intervals.sort(key=lambda x:x[0])
        ans = []

        i = 0
        while i < len(intervals):
            start = i
            end = i

           #merge the arrays
            while i + 1 < len(intervals) and intervals[i + 1][0] <= intervals[end][1]:
                if intervals[i + 1][1] > intervals[end][1]: #make the end the greatest ending digit
                    end = i + 1
                i += 1
            
            if start == i:
                ans.append([intervals[i][0], intervals[i][1]])
            else:
                ans.append([intervals[start][0], intervals[end][1]])
            i += 1
        return ans

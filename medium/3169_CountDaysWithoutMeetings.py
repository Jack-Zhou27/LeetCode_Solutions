class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        #init
        meets = []
        for start, end in meetings:
            meets.append((start, end))

        meets = sorted(meets, key=lambda x: x[0]) #sort meetings by start time
        
        #algo
        totals = 0
        prevStart = 0
        prevEnd = 0
        for start, end in meets:
            if start > prevEnd: # if meetings don't overlap at all
                totals += end - start + 1
                prevEnd = end
            elif end > prevEnd: # if meetings overlap
                totals += end - prevEnd
                prevEnd = end

        return days - totals

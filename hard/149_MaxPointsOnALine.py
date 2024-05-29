class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        #Handle edge cases
        if(len(points) <= 2):
            return len(points)

        #We know two points make a line, so our min ans is 2
        ans = 2

        #For each point, calculate it's slope to all the other points
        #and count how many times the same slope occurs. Then, take the max of that count.
        for i in range (0, len(points) - 1):
            hashMap = {}
            tempMax = 0
            for j in range (i + 1, len(points)):
                rise = points[j][1] - points[i][1]
                run = points[j][0] - points[i][0]
                slope = 0
                if(run == 0):
                    slope = float("inf")
                else:
                    slope = rise/run

                if(slope in hashMap):
                    hashMap[slope] = hashMap[slope] + 1
                    tempMax = max(tempMax, hashMap[slope])
                else:
                    hashMap[slope] = 2
            
            ans = max(tempMax, ans)
        return ans

                

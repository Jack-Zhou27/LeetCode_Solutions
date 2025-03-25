class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        i = 0
        for x, y in points:
            dist = x * x + y * y
            heappush(minHeap, (dist, [x, y]))
        
        ans = []
        for i in range(k):
            dist, pt = heappop(minHeap)
            ans.append(pt)
        return ans

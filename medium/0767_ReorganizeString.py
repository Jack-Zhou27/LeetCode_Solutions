class Solution:
    def reorganizeString(self, s: str) -> str:
        
        #init maxHeap
        counts = {}
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        maxHeap = []
        for key, val in counts.items():
            heappush(maxHeap, (-1 * val, key))
        
        #algo 
        ans = ""
        while len(maxHeap) > 0:
            val, key = heappop(maxHeap)
            while val < -1: #note that our maxheap has negative nums as python only has minheap
                if len(maxHeap) <= 0:
                    return ""
                    
                nextVal, nextKey = heappop(maxHeap)
                ans += key
                ans += nextKey
                val += 1

                if nextVal + 1 < 0:
                    heappush(maxHeap, (nextVal + 1, nextKey))
            ans += key
            
        return ans

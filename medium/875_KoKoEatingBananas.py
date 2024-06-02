class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
        #compute how many hours are used if we eat k bananas at a time
        def hoursused (k, piles):
            res = 0
            for i in piles:
                res += math.ceil(i/k)
            return res 
        
        #binary search for our answer (the smallest k)
        left = 1
        right = max(piles) 
        while(left <= right):
            middle = (left + right) // 2
            temp = hoursused(middle, piles)
            if(temp > h):
                left = middle + 1
            else:
                right = middle - 1
        
        return left #we don't return middle, but left bc using middle as our k can have situations where not all bananas are eaten in time

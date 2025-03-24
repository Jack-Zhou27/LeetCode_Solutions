class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1 for i in range(0, len(ratings))]
       
        #forward pass
        for i in range(0, len(ratings)):
            if(i - 1 >= 0 and ratings[i] > ratings[i - 1]):
                candy[i] = candy[i - 1] + 1
        
        #backward pass
        for i in range(len(ratings) - 1, -1, -1):
             if(i + 1 < len(candy) and ratings[i] > ratings[i + 1]):
                candy[i] = max(candy[i], candy[i + 1] + 1) #take the max value of the candy from forward/backward passes
      
        return sum(candy)

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        #compute the sum of the pairs
        total = sum(skill)
        if total % (len(skill) // 2) != 0:
            return -1
        skills = (int)(total // (len(skill) // 2))
       
        #create a frequency list (we are approaching the problem like: Two Sum)
        complement = {}
        for i in skill:
            if i in complement:
                complement[i] += 1
            else:
                complement[i] = 1
        
        #algorithm
        chemistry = 0
        for i in skill:
            #Note player i in skill is renamed player skills - i in complement.
            #Thus, we check if our current player (skills - i) and our complement player (i) exists in the COMPLEMENT list. This may be a little confusing, but we flip it because we are analyzing the complement array and not the skills array here. 
            if i not in complement or skills - i not in complement:
                return -1
            
            #the order of the if statements are important here, because we need to remove two players from our complement list each time we find a pair, so we must continue if this condition (the player that we previously removed is not in the complement list) is met and not return -1
            if complement[skills - i] == 0:
                continue

             #if we used up all of our complement players, return 0 since we cannot find a valid pair
            if complement[i] == 0:
                return -1
            
            #update complement list and chemistry
            chemistry += (i * (skills - i))
            complement[i] -= 1
            complement[skills - i] -= 1
        return chemistry




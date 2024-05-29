class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        #create a list called values the stores the cost to convert each word
        values = []
        s1 = list(s)
        t1 = list(t)
        
        for i in range(0, len(s1)):
            values.append(abs(ord(s1[i]) - ord(t1[i])))

        ans = 0
        left = 0
        right = 0
        total = 0
        temp = 0

        #we use two pointers
        while(right < len(values)):

            #create the largest substring possible that's within the cost
            while(right < len(values) and total <= maxCost):
                total += values[right]
                right += 1
                temp += 1
              
            #check if this substring's length can be our answer
            ans = max(ans, temp - 1)

            #since we made the total value of the substring overshoot the cost intially, we need to readjust
            while(left < right and total > maxCost):
                total -= values[left]
                left += 1
                temp -= 1

            #check if this substring's length can be our answer
            ans = max(ans, temp)
        return ans

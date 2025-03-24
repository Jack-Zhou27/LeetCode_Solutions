class Solution:
    def largestVariance(self, s: str) -> int:
        #init
        unique_temp = set()
        unique = []
        for c in s:
            if c in unique_temp:
                continue
            else:
                unique_temp.add(c)
                unique.append(c)

        def variance(a, b):
            count_a = 0
            count_b = 0
            remaining_b = s.count(b)
            ans = 0
            for c in s:
                if c == a:
                    count_a += 1
                elif c == b:
                    count_b += 1
                    remaining_b -= 1

                if count_b > 0:
                    ans = max(ans, count_a - count_b)
            
                if count_a - count_b < 0 and remaining_b > 0:
                    count_a = 0
                    count_b = 0
            return ans


        ans = 0
        for l in range(len(unique)):
            for r in range(len(unique)):
                if l != r:
                    ans = max(ans, variance(unique[l], unique[r]))
        
        return ans

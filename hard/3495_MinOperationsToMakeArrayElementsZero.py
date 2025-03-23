class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        import math

        ans = 0
        cutoffs = []
        cutoffs.append(1)
        #init cutoffs -> 1..3 is 1 operation, 4..15 is 2 operations etc.
        for i in range(1, 18):
            cutoffs.append(4 * cutoffs[i - 1])

        for arr in queries:
            totals = 0

            l = arr[0]
            r = arr[1]

            currCutoff = 0

            #to count total, this is the naive method that times out...
            # for i in range(l, r + 1):
            #     while(cutoffs[currCutoff] <= i):
            #         currCutoff += 1
            #     totals += currCutoff

            #speed up by using pure maths
            while(cutoffs[currCutoff] <= r):
                currCutoff += 1
                if cutoffs[currCutoff] <= l:
                    continue

                totals += currCutoff * (cutoffs[currCutoff] - l)
                l = cutoffs[currCutoff]
            totals += currCutoff * (r - l + 1) 

            #handle odd offset
            ans += totals //2 
            if totals % 2 != 0:
                ans += 1

        return ans

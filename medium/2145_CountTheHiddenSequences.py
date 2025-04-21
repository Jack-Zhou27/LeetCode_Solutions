class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefixSum = [0]
        smallest = float('inf')
        largest = -float('inf')
        for i in differences:
            curr = prefixSum[-1] + i
            prefixSum.append(curr)
            if curr > largest:
                largest = curr
            if curr < smallest:
                smallest = curr
        
        lowerbound = max(lower, lower - smallest) 
        upperbound = min(upper, upper - largest) 
        
        if upperbound >= lowerbound:
            return upperbound - lowerbound + 1
        return 0

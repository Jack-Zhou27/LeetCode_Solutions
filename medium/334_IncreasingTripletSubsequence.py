class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        #HERE'S THE THING: i < j < k technically does not matter!!!

        """
        When we go through the array, the absolutle smallest number we
        see up to that current point will be assigned to first, and 
        then the absolutle second smallest number that we see up to 
        that point will be assigned to second (which is greater 
        than first). But when we assign new values to second,
        since second is allways going to be greater than ALL
        PREVIOUS INSTANCES of first, then the index rder of i < j 
        was not messed up. Now, if we see another number that 
        is bigger than first and second, then we knew a valid
        triplet exists. This logic is quite tricky.
        """
        
        first = second = float("inf")
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False


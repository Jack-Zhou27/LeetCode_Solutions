# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            m = (r - l) // 2 + l
            g = guess(m)
            if g == 0:
                return m
            elif g == 1:
                l = m + 1
            else:
                r = m - 1
        return -1

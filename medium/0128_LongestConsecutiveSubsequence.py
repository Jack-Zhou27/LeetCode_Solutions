class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #handle edge cases
        if(len(nums) <= 1):
            return len(nums)

        ans = 1
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 0 # 0 means unvisited

        #key: the number | value: how many consecutive numbers can branch off that number

        #loop through all the keys
        for i in hashMap.keys():
            #if key + 1 (the next consecutive number) exists, and that next consecutive number has been visited...
            if(i + 1 in hashMap and hashMap[i + 1] != 0):
                hashMap[i] = hashMap[i + 1] + 1
                ans = max(ans, hashMap[i])
                continue
            
            #mark this key as visited and see how many conseutive numbers can branch off this key
            count = 0
            j = i
            while(j in hashMap):
                j += 1
                count += 1

            #update the keys with its corresponding value of how many consecutive numbers it has
            #we are esentially creating a cache, storing the values of the keys that we have
            #visited already
            for k in range(i, j):
                hashMap[k] = count - (k - i)
            ans = max(ans, hashMap[i])

        return ans


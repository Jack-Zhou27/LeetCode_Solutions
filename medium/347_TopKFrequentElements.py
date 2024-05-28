class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create a frequency map of how many times each number occurs
        numMap = {}
        for i in nums:
            if(i in numMap):
                numMap[i] = numMap[i] + 1
            else:
                numMap[i] = 1

        #sort the map by its values in descending order (largest -> smallest)
        numMap = dict(sorted(numMap.items(), key=lambda x:x[1], reverse = True))

        #take the first k keys in your map (what the question asks for)
        ans = []
        count = 0
        for keys in numMap:
            ans.append(keys)
            if(count >= k - 1):
                break
            count += 1
        return ans
        

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort()
        for i in range(0, len(citations)):
            if(citations[i] >= len(citations) - i):
                return len(citations) - i
        
        return 0
            


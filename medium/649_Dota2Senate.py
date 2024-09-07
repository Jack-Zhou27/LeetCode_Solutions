class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #we directly simulate the description.
            #1) The senator at the earlier index eliminates the first occurenct of the opposite senator at a later index
            #2) After this senator has moved, move him to the back of the line (the queue) 

        queueD = deque()
        queueR = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                queueR.append(i)
            else:
                queueD.append(i)

        while len(queueD) != 0 and len(queueR) != 0:
            size = len(queueD) + len(queueR)
            l = queueD.popleft()
            r = queueR.popleft()
            if l < r:
                queueD.append(l + size)
            else:
                queueR.append(r + size)

        return "Radiant" if len(queueD) == 0 else "Dire"

      
        
            

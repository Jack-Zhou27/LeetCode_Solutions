class RecentCounter:

    def __init__(self):
        self.requests = []
        
    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests and self.requests[0] < t - 3000:
            self.requests.pop(0)
        
        return len(self.requests)

        #NOTE: by not popping what's on the left, we make our sol too slow.
        #Since t is strictly increasing, those values out of bounds on the left
        #will never be needed again, so save computation by popping them.

        #TOO SLOW: 
        # index = 0
        # while index < len(self.requests):
        #     if self.requests[index] < self.requests[-1] - 3000:
        #         index += 1
        #     else:
        #         break
        
        # return len(self.requests) - index
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

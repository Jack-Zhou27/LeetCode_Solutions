class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []
        self.day = 0

    def next(self, price: int) -> int:

        #create monotonic decreasing stack
        self.day += 1
        while(self.monotonic_stack and price > self.monotonic_stack[-1][0]):
            self.monotonic_stack.pop()
        self.monotonic_stack.append((price, self.day))

        #find how many days are less than or equal 
        ans = 0
        i = 0
        n = len(self.monotonic_stack)
        while i < n and self.monotonic_stack[i][0] > price:
            i += 1
        
        #edge case
        if i == 0 or len(self.monotonic_stack) == 1:
            return self.day

        ans += self.day - self.monotonic_stack[i - 1][1]
        return ans




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

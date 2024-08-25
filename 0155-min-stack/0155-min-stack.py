class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.min_stack or val<= self.min_stack[-1] :
            self.min_stack.append(val) 
        else:
            self.min_stack.append(self.min_stack[-1])
        self.stack.append(val)
        return self.stack

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
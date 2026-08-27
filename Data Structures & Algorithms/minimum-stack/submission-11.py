class MinStack:

    def __init__(self):
       self.stack = []
       self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        currMin = val if not self.minVals else min(val, self.minVals[-1])
        # Always push the smallest value
        self.minVals.append(currMin)

    def pop(self) -> None:
        temp = self.stack.pop()
        self.minVals.pop()
            
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]

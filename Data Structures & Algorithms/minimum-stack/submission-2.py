class MinStack:

    def __init__(self):


        self.stack = []
        self.minVal = None
        

    def push(self, val: int) -> None:

        self.minVal = val if (self.minVal == None or self.minVal > val) else self.minVal

        self.stack.append(val)
        

    def pop(self) -> None:

        if self.stack:

            pop = self.stack.pop()
            if pop == self.minVal:
                self.minVal = min(self.stack) if self.stack else None


        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.minVal


        

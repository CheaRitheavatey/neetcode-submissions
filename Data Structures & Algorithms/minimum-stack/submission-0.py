class MinStack:

    def __init__(self):
        self.stack = []
        self.num = float('inf') 

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.num = min(self.num, val)


    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        num = self.stack[-1]
        return num
        

    def getMin(self) -> int:

        if not self.stack:
            return null

        x = float('inf') 
        for i in self.stack:
            if i < x:
                x = i
        return x
        

        

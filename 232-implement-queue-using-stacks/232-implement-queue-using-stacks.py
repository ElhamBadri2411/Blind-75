class MyQueue:

    def __init__(self):
        self.stack_one = []
        self.stack_two = []
    

    def push(self, x: int) -> None:
        self.stack_one.append(x)

    def pop(self) -> int:
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
            
        res = self.stack_two.pop()
        
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
        
        return res

    def peek(self) -> int:
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
        
        res = self.stack_two[-1]
        
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
            
        return res
        
    def empty(self) -> bool:
        if not self.stack_one and not self.stack_two:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
from bisect import insort
class MinStack:
    def __init__(self):
        self.data = []
        self.data_ordered = []

    def push(self, val: int) -> None:
        self.data.append(val)
        insort(self.data_ordered, val)
        

    def pop(self) -> None:
        elem = self.data.pop()
        self.data_ordered.remove(elem)
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.data_ordered[0]
        

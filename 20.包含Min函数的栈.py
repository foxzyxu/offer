class StackwithMin():
    def __init__(self):
        self.val = []
    
    def push(self, x):
        self.val.append(x)
    
    def take(self):
        self.val.pop()
    
    def findMin(self):
        return min(self.val)
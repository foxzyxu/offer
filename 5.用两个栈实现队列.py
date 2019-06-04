class stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        
    def push(self,val):
        self.stack1.append(val)
#        压入
    
    def pop(self):
        if self.stack1:
            self.stack2=self.stack1.reverse()
        while self.stack2:
            return self.stack2.pop()
#        弹出


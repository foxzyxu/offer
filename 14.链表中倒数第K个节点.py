def node(self,val):
    self.head = val
    self.next = None

class method():
    def find(self,pin,k):
        if pin == None or pin.next == None:
            return pin
        pre = None
        while pin:
            after = pin.next
            pin.next = pre
            pre = pin
            pin = after
            for i in range(0,k):
                pin.next = after
                pin = after
            return pin        
            

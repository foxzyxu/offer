class onenode():
    def __init__(self,item):
        onenode.item = item
        onenode.next = None

class nodelist():
    def __init__(self):
        self._head = None
    def headadd(self,item):
        node = onenode(item)
        node.next = self._head
        self._head = node
    def printlist(self):
        pin = self._head
        while pin != None:
            print(pin.item)
            pin = pin.next

if __name__ == '__main__':
    list = nodelist()
    list.headadd(1)
    list.headadd(2)
    list.printlist()
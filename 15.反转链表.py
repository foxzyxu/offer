class listnode():
    def __init__(self,n):
        self.val = n
        self.next = None

class method():
    def converse(self,node):
        if node == None or node.next == None:
            return node
        pre = None
        while node:
            after = node.next
            node.next = pre
            pre = node
            node = after
        return node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class method:
    def mutualNode(self, Head1, Head2):
        # write code here
        list1 = []
        list2 = []
        pin1 = Head1
        pin2 = Head2
        while node1:
            list1.append(node1.val)
            pin1 = pin1.next
        while pin2:
            if pin2.val in list1:
                return pin2
            else:
                pin2 =pin2.next

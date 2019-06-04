#**题目：**输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一
#个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要
#返回参数中的节点引用，否则判题程序会直接返回空）。
#
#**思路：**将大问题转变为小问题，每次都进行复制头部节点，然后进行递归，每次同样处理头部节点。
class listnode():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.ran = None
        

class method():
    def clone(pHead):
        if pHead == None:
            return None
        #复制节点在原节点之后
        pCur = pHead
        while(pCur != None):
            node = listnode(pCur.label)
            node.next = pCur.next
            pCur.next = node
            pCur = node.next
        #复制random节点
        pCur = pHead
        while(pCur != None):
            if pCur.random != None:
                pCur.next.random = pCur.random.next
            pCur = pCur.next.next
        head = pHead.next
        cur = head
        #将新旧链表分离
        pCur = pHead
        while(pCur != None):
            pCur.next = pCur.next.next
            if cur.next != None:
                cur.next = cur.next.next
            cur = cur.next
            pCur = pCur.next
        return head
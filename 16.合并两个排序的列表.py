#**题目：**输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
#**题解：**将两个链表之中的数值转换到列表之中，并进行排序，将排序后的列表构造成链表。
class listnode():
    def __init__(self, x):
        self.val = x
        self.next = None

class method():
    list1, list2 = [], []
    def merge(self, head1, head2):
        if head1 == None and head2 == None:
            return None
        while head1:
            list1.append(head1.val)
            head1 = head1.next
        while head2:
            list2.append(head2.val)
            head2 = head2.next
        mergedlist = list1 + list2
        mergedlist.sort
        head3 = listnode(mergedlist[0])
        pre = head3
        for i in range(1,len(mergedlist)):
            node = listnode(mergedlist[i])
            pre.next = node
            pre = pre.next
        return head
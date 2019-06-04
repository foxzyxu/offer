#题目：**给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，
#树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
#思路：
#该节点有右子树
#该节点没有右子树
#第一种比较处理起来比较简单，直接将其右节点进行中序遍历即可，并将一个遍历到的最右节点
#返回。
#第二种情况又分为两种情况
#该节点是父节点的左子节点
#该节点是父节点的右子节点
#这里，该节点是父节点的左子节点的这种情况比较简单，直接将父节点返回即可
#如果是父节点的右子节点的话，需要不断的向上移动，直到对应的节点不是父节点的右节点（即
#左节点），，既然他是父节点的左节点，此时将这个节点父节点返回即可，或者遍历到了根节点
#，返回null；

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.father = None
class method():
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:
            left1=pNode.right
            while left1.left:
                   left1=left1.left
            return left1

        while pNode.next:
            tmp=pNode.next
            if tmp.left==pNode:
                return tmp
            pNode=tmp
    
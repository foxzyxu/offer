#**题目：**输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任
#何新的结点，只能调整树中结点指针的指向。
#**思路：**递归将根结点和左子树的最右节点和右子树的最左节点进行连接起来。
class treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return pRootOfTree
        if pRootOfTree.left is None and pRootOfTree.right is None:
            return pRootOfTree

        #处理左子树
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left

        if left:
            while left.right:
                left=left.right
            pRootOfTree.left,left.right=left,pRootOfTree

        #处理右子树
        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right

        if right:
            while right.left:
                right=right.left
            pRootOfTree.right,right.left=right,pRootOfTree

        while pRootOfTree.left:
            pRootOfTree=pRootOfTree.left
        return pRootOfTree

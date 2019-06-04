# 空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self,root):
        if root is None:
            return 0
        left=self.TreeDepth(root.left)
        right=self.TreeDepth(root.right)
        return max(left+1,right+1)

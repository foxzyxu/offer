#**题目：**输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
#路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)。
#**思路：**利用递归的方法，计算加左子树和右子树之后的值，当参数较多是，可以将结果添加到函数变量之中。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class method():
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        ans=[]
        path=[]
        self.dfs(root,expectNumber,ans,path)
        ans.sort()
        return ans

    def dfs(self,root,target,ans,path):
        if not root:
            return

        path.append(root.val)
        if root.left is None and root.right is None and target==root.val:
            ans.append(path[:])

        if root.left:
            self.dfs(root.left,target-root.val,ans,path)
        if root.right:
            self.dfs(root.right,target-root.val,ans,path)

        path.pop()
#比较好的做法是将path设为全局的，然后dfs的过程便是先序遍历的过程，一旦遍历到叶子结点，
#便将path最后的节点移除掉，这样在递归一层一层进行的时候将值添加进path,在递归返回的过程
#中将path最末尾的元素一个一个移除。这样便依靠递归的特性完成了路径的恢复。
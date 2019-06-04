#题目：**给定一棵二叉搜索树，请找出其中的第k小的结点。例如（5，3，7，2，4，6，8）中，
#按结点数值大小顺序第三小结点的值为4。
#首先这个是一颗二叉搜索树，我只需要是的这个这颗二叉搜索树进行排序，然后找到第k个
#，那个我们都知道二叉搜索树的中序遍历是一个有顺序的序列，这个时候我就是要中序遍历这颗
#二叉树，然后设置一个变量，访问一个变量的时候就加一，判断这个变量和k是否相等，如果相
#等，则将当前的这个结点返回即可。
count = 0
def KthNode(self, pRoot, k):
    if not pRoot:
        return None
    node = self.KthNode(pRoot.left, k)
    if node:
        return node
    self.count += 1
    if self.count == k:
        return pRoot
    node = self.KthNode(pRoot.right, k)
    if node:
        return node

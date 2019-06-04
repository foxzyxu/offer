#**题目：**请实现两个函数，分别用来序列化和反序列化二叉树。
#**思路：**转变成前序遍历，空元素利用"#"代替，然后进行解序列。
#有#占位空节点，比重构简单
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def Serialize(self, root):
    if not root:
        return '#'
    return str(root.val) +',' + self.Serialize(root.left) +','+ self.Serialize(root.right)
def Deserialize(self, s):
    list = s.split(',')
    return self.deserializeTree(list)

def deserializeTree(self, list):
    if len(list)<=0:
        return None
    val = list.pop(0)
    root = None
    if val != '#':
        root = TreeNode(int(val))
        root.left = self.deserializeTree(list)
        root.right = self.deserializeTree(list)
    return root
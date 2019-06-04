#**题目：**输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）。
#**题解：**将树转变为中序序列，然后转变为str类型，最后判断是否包含。
class treenode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class method():
    def inorder(self, root, travel = []):
        if root == None:
            return False
        self.inorder(root.left)
        travel.append(root.val)
        self.inorder(root.right)
        
    def judgement(self, root1, root2):
        if root1 == None or root2 == None:
            return False
        travel1, travel2 = [], []
        self.inorder(root1, travel1)
        self.inorder(root2, travel2)
        str1 = ''.join(str(i) for i in travel1)
        str2 = ''.join(str(i) for i in travel2)
        if str1 in str2:
            return True
        else:
            return False
    
        
        
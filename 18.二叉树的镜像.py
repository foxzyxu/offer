class treenode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class method():
    def mirror(self, root):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        temp=root.left
        root.left=root.right
        root.right=temp

        if root is not None:
            self.Mirror(root.left)
        if root is not None:
            self.Mirror(root.right)

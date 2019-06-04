class treenode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self. right = None


class method():
    def widetravel(self, root):
        if not root:
            return []
        ans = []
        temp = []
        temp.append(root)

        while temp:
            currentRoot = temp.pop(0)
            ans.append(currentRoot.val)
            if currentRoot.left:
                temp.append(currentRoot.left)
            if currentRoot.right:
                temp.append(currentRoot.right)
        return ans

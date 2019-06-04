class treenode():
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

def reconstruct(self,pre,mid):
    root = treenode(pre[0])
    for i in range(0,len(pre)):
        if pre[0] == mid[i]:
            return i
    root.left = reconstruct(pre[1:i+1],mid[:i])
    root.right = reconstruct(pre[i+1:],mid[i+1:])
    return root

if __name__ == '__main__':
    pre = [1,2,4,7,3,5,6,8]
    mid = [4,7,2,1,5,3,8,6]
    tree = reconstruct(pre,mid)
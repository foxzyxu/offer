class treenode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class method:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence)==1:
            return True
        i=0
        while sequence[i]<sequence[-1]:
            i=i+1
        k=i
        for j in range(i,len(sequence)-1):
            if sequence[j]<sequence[-1]:
                return False
        leftsequence=sequence[:k]
        rightsequence=sequence[k:len(sequence)-1]
        if len(leftsequence)>0:
            self.VerifySquenceOfBST(leftsequence)
        if len(rightsequence)>0:
            self.VerifySquenceOfBST(rightsequence)
        return True

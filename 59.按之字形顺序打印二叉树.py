#层次遍历的一种优化
class Solution:
    def Print(self, pRoot):
        # write code here
        root=pRoot
        if not root:
            return []
        level=[root]
        result=[]
        righttoleft=False
        while level:
            curvalues=[]
            nextlevel=[]
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if righttoleft:
                    curvalues.reverse()
            if curvalues:
                    result.append(curvalues)
            level = nextlevel
            righttoleft = not righttoleft
        return result
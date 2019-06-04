#题目：**从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
#依然是层次遍历的变形
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        root=pRoot
        if not root:
            return []
        level=[root]
        result=[]
        while level:
            curvalues=[]
            nextlevel=[]
            for i in level:
                curvalues.append(i.val)
                if i.left:
                    nextlevel.append(i.left)
                if i.right:
                    nextlevel.append(i.right)
            if curvalues:
                    result.append(curvalues)
            level = nextlevel
        return result

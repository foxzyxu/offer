#**题目：**输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
#假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
#但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）。
class method:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV)==1 and len(popV)==1 and pushV[0]!=popV[0]:
            return False

        helpV=[]
        pushV.reverse()
        popV.reverse()
        helpV.append(pushV[len(pushV)-1])
        pushV.pop()
        while True:
            if helpV[len(helpV)-1]!=popV[len(popV)-1]:
                helpV.append(pushV[len(pushV)-1])
                pushV.pop()

            if helpV[len(helpV)-1]==popV[len(popV)-1]:
                helpV.pop()
                popV.pop()

            if pushV==[] and popV==[] and helpV==[]:
                return True

            if pushV==[] and popV[len(popV)-1]!=helpV[len(helpV)-1]:
                return False

#题目：**求1+2+3+…+n，要求不能使用乘除法、for、while、if、else、switch、case等关
#键字及条件判断语句（A?B:C）
class method():
    def sumN(self, n):
        return n>0 and self.sumN(n-1)+n
        
    
if __name__=='__main__':
    n=6
    method=method()
    ans=method.sumN(n)
    print(ans)

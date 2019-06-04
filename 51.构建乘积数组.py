# 题目
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
class method():
    def multipleofb(self,  a):
        b = [1 for i in range(0, len(a))]
        for i in range(0, len(a)):
            for i in range(0, len(a)):
                if i !=j:
                    b[i] *= a[j]
        return b
                    
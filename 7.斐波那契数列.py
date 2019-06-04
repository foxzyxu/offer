class method:
    def fibo(self,n):
        if n==1:
            return 1
        if n==2:
            return 2
        if n>2:
            fibo_list=[1,2]
            for i in (0,n-3):
                fibo_list[0],fibo_list[1]=fibo_list[1],fibo_list[0]+fibo_list[1]
            return fibo_list[1]
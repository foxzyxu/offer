class method:
    def jumpbox(self,n):
        if n==0:
            return 0
        if n==1:
            return 1        
        if n==2:
            return 2
        if n>2:
            fibo_list=[1,2]
            for i in (3,n+1):
                fibo_list[0],fibo_list[1]=fibo_list[1],fibo_list[0]+fibo_list[1]
                return fibo_list[1]
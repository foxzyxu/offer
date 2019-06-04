class method():
    def  findnum(self,numlist):
        tem = numlist[0]
        times = 1
        for i in range(1,len(numlist)):
            if numlist[i] == tem:
                times +=1
            if numlist[i] != tem:
                times -=1
            if times == 0:
                tem = numlist[i]
                times = 1
        if times > 0:
            return tem
        if times <= 0:
            return 0
        
if __name__=='__main__':
    numlist = [1, 2, 2, 2, 2, 3, 3]
    method=method()
    ans=method.findnum(numlist)
    print(ans)

            
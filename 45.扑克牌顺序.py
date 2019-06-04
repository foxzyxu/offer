class method():
    def concession(self, pokers):
        pokers.sort()
        ghost = 0
        for i in range(0,len(pokers)):
            if pokers[i] == 0:
                ghost += 1
        for i in range(ghost+1,len(numbers)):
            if numbers[i]==numbers[i-1]:
                return False        
        if pokers[-1]-pokers[ghost] <= ghost:
            return True
        else:
            return False
        
        
        
if __name__=='__main__':
    numbers=[1,0,0,6,0]
    method=method()
    ans=method.concession(numbers)
    print(ans)
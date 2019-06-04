
def NumberOf1Between1AndN_Solution(self, n):
    mult, sumTimes = 1, 0 
    while n//mult > 0:
        high, mod = divmod(n, mult*10) 
        curNum, low = divmod(mod, mult) 
        if curNum > 1:
            sumTimes += high*mult + mult 
        elif curNum == 1:
            sumTimes += high*mult + low + 1 
        else: 
            sumTimes += high*mult 
        mult = mult*10 
        
    return sumTimes
                
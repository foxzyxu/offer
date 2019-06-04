#等差数列公式  2*n*a1+n(n-1)/2 = s; 由n>= 2 得 a1 <= (s - 1)/2
#对首位数字a1从1到 (s - 1)/2遍历
#等差数列公式变形   n*n+(2*a1 - 1)n-2s = 0
#可得n = [-(2a - 1) + sqrt((2a - 1) * (2a - 1) + 8s)]/2
#检验n是否为整数，是则得到一个答案
class method:
    def FindContinuousSequence(self, tsum):
        # write code here
        ans=[]
        for i in range(1,tsum//2+1):
            oneans=[]
            for k in range(1,tsum):
                tempsum=((i+i+k-1)*k)//2
                if tempsum==tsum:
                    for j in range(i,i+k):
                        oneans.append(j)
                    break
            if oneans !=[]:
                ans.append(oneans)
        return ans

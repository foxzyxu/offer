#数列满足递增，设两个头尾两个指针i和j，
# 1、若ai + aj == sum，就是答案（相差越远乘积越小）
# 2、若ai + aj > sum，aj肯定不是答案之一（前面已得出 i 前面的数已是不可能），j -= 1
# 3、若ai + aj < sum，ai肯定不是答案之一（前面已得出 j 后面的数已是不可能），i += 1
#第一，小的数字在前面，这个没问题。第二，题目中要求当存在多个组合的时候，返回其中的乘
#积最小的一个。我们从两头向中间的移动过程中找到的第一组一定是乘积最小的。原因如下：
#我们把两个数字想成矩形的两条边，根据中学的知识，当两条边越接近，面积越大（乘积越大）。
#由于从两头向中间进行查找的，找到的第一个组合一定是边差距最大的，所以乘积最小。
class method:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        ans=[]
        i,j,minres=0,len(array)-1,1000000
        for i in range(0,len(array)-1):
            j=len(array)-1
            while True:
                tempsum = array[i] + array[j]
                if tempsum == tsum:
                    if array[i]*array[j]<minres:
                        ans=[]
                        ans.append(array[i])
                        ans.append(array[j])
                        minres=array[i]*array[j]
                    break
                else:
                    j = j - 1
                if tempsum<tsum:
                    break
                if j<=i:
                    break
        return ans
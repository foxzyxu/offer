class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dict={}
        for num in array:
            dict[num]=0
        for i in range(0,len(array)):
            dict[array[i]]=dict[array[i]]+1
        ans=[]
        for num in array:
            if dict[num]==1:
                ans.append(num)
        return ans

if __name__=='__main__':
    array=[1,1,2,2,3,3,4,5,5,6,7,7]
    solution=Solution()
    ans=solution.FindNumsAppearOnce(array)
    print(ans)

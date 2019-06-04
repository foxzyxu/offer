class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        for i in range(0,len(numbers)):
            for j in range(i,len(numbers)):
                if int(str(numbers[i])+str(numbers[j]))>int(str(numbers[j])+str(numbers[i])):
                    numbers[i],numbers[j]=numbers[j],numbers[i]
        ans=''
        for i in range(0,len(numbers)):
            ans=ans+str(numbers[i])
        return ans

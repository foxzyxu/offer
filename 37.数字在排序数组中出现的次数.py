class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        ans=0
        for i in range(0,len(data)):
            if data[i]==k:
                ans=ans+1
            if data[i]>k:
                break
        return ans

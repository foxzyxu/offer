class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        maxsum,tempsum=array[0],array[0]
        for i in range(1,len(array)):
            if tempsum<0:
                tempsum=array[i]
            else:
                tempsum = tempsum + array[i]
            if tempsum>maxsum:
                maxsum=tempsum
        return maxsum
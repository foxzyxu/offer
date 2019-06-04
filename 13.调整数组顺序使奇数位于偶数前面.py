class Solution:
    def reOrderArray(self, array):
        # write code here
        array1=[]#奇数
        array2=[]#偶数
        for i in range(0,len(array)):
            if array[i]%2!=0:
                array1.append(array[i])
            else:
                array2.append(array[i])
        array3=array1+array2
        return array3

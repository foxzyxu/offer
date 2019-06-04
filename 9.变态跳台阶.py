class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 2
        return 2*self.jumpFloorII(number-1)

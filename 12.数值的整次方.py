class Solution:
    def Power(self, base, exponent):
        val=1
        for i in range(0,abs(exponent)):
            val *=base
        if exponent>0:
            return val
        if exponent>0:
            return False
        else:
            return 1/val

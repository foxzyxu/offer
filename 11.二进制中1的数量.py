class Solution:
    def NumberOf1(self, n):
        count = 0
        for i in range(32):
            count += (n >> i) & 1
        return count

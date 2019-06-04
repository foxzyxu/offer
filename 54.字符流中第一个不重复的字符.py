class Solution:
    # 返回对应char
    def __init__(self):
        self.all={}
        self.ch=[]
    def FirstAppearingOnce(self):
        # write code here
        if self.all is None:
            return '#'
        for c in self.ch:
            if self.all[c]==1:
                return c
        return '#'

    def Insert(self, char):
        # write code here
        self.ch.append(char)
        if char in self.all:
            self.all[char]=self.all[char]+1
        else:
            self.all[char]=1
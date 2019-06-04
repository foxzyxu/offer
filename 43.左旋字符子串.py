class method:
    def LeftRotateString(self, s, n):
        # write code here
        if s=='' and n==0:
            return ''
        ans=''
        ans=s[n:]+s[0:n]
        return ans
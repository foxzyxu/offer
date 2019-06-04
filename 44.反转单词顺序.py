class method:
    def ReverseSentence(self, s):
        # write code here
        ans,word=[],''
        for i in range(0,len(s)):
            word = word + s[i]
            if s[i]==' ':
                ans.append(word)
                word=''
            if i==len(s)-1:
                word=word+' '
                ans.append(word)
        ans.reverse()
        res=''
        for c in ans:
            res=res+c
        return res[:len(res)-1]
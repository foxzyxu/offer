class method:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        sset=set(s)
        dict={}
        for c in sset:
            dict[c]=0
        for i in range(0,len(s)):
            dict[s[i]]=dict[s[i]]+1
        onetime=[]
        for c in dict:
            if dict[c]==1:
                onetime.append(c)

        if onetime is None:
            return -1
        else:
            index=0
            for i in range(0,len(s)):
                if s[i] in onetime:
                    index=i
                    break
            return index
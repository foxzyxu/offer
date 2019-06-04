#题目：**将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string
#不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是
#一个合法的数值则返回0
class method():
    def StrToInt(self, s):
        res,mult,flag = 0,1,1
        if not s:
            return res
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                flag = -1
            s = s[1:]
        for i in range(len(s)-1, -1, -1):
            if '9' >= s[i] >= '0':
                res += (ord(s[i]) - 48)*mult
                mult = mult * 10
            else:
                return 0
        return res*flag
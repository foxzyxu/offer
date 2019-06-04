#题目：**写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号
class method():
    def Add(self, num1, num2):
        # write code here
        while num2!=0:
            sum=num1^num2
            carry=(num1&num2)<<1
            num1=sum
            num2=carry
        return num1

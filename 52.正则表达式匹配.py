#题目：**请实现一个函数用来匹配包括’.‘和’*‘的正则表达式。模式中的字符’.‘表示任意一个
#字符，而’*'表示它前面的字符可以出现任意次（包含0次）。在本题中，匹配是指字符串的所有
#字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"
#均不匹配
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if s == pattern:
            return True
        if not pattern:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if (s and s[0] == pattern[0]) or (s and pattern[0] == '.'):
                return self.match(s, pattern[2:]) \
                       or self.match(s[1:], pattern) \
                       or self.match(s[1:], pattern[2:])
            else:
                return self.match(s, pattern[2:])
        elif s and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False
class Solution:
    def maxInWindows(self, num, size):
        que = [0]
        list1 = []
        if len(num) == 0 or size <= 0 or num == None:
            return list1
        if size == 1 :
            list1.append(num[que[0]])
        for i in range(1, len(num)):
            if i - size >= que[0]:
                que.pop(0)
            while (len(que) != 0 and num[i] > num[que[-1]]):
                que.pop(-1)
            que.append(i)
            if i >= size - 1:
                list1.append(num[que[0]])
        return list1
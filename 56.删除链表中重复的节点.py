class Solution:
    def deleteDuplication(self, pHead):
        first = ListNode(-1)
        first.next = pHead
        curr = pHead
        last = first
        while curr and curr.next:
            if curr.val != curr.next.val:
                curr = curr.next
                last = last.next
            else:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                last.next = curr
        return first.next
from hkdsun.linkedlist import *


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = i1 = i2 = head
        prev = None
        while n:
            i2, n = i2.next, n-1
        while i2:
            prev, i1, i2 = i1, i1.next, i2.next
        if prev:
            prev.next = i1.next
        else:
            return h.next
        return h

l = ListNode.build([1, 2, 3, 4, 5])
l = ListNode.build([1, 2])
l = ListNode.build([1])
print Solution().removeNthFromEnd(l, 1)

from hkdsun.linkedlist import *


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        k %= n
        if k == 0:
            return head
        l = r = head
        for i in range(k):
            r = r.next
        while r.next:
            l, r = l.next, r.next
        res = l.next
        l.next = None
        r.next = head
        return res

print Solution().rotateRight(ListNode.build([1, 2, 3, 4, 5]), 5)

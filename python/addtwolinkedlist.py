from hkdsun.linkedlist import *


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = None
        head = None
        while l1 and l2:
            if res:
                res.next = ListNode(0)
                res = res.next
            else:
                res = ListNode(0)
                head = res
            v = l1.val + l2.val + carry
            if v >= 10:
                carry, v = 1, v % 10
            else:
                carry = 0
            res.val = v
            l1, l2 = l1.next, l2.next
        while l1:
            res.next = ListNode(0)
            res = res.next
            v = l1.val + carry
            if v >= 10:
                carry, v = 1, v % 10
            else:
                carry = 0
            res.val = v
            l1 = l1.next
        while l2:
            res.next = ListNode(0)
            res = res.next
            v = l2.val + carry
            if v >= 10:
                carry, v = 1, v % 10
            else:
                carry = 0
            res.val = v
            l2 = l2.next
        if carry == 1:
            res.next = ListNode(1)
        return head


l = ListNode.build([1, 0, 6])
r = ListNode.build([1, 1, 1, 1, 1, 1])
print Solution().addTwoNumbers(l, r)

from hkdsun.linkedlist import *


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        if head.val == val:
            head = head.next
        return head


    def removeElements1(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        prev, cur = head, head.next
        while prev.val == val:
            if not cur:
                return None
            prev, cur = cur, cur.next
        res = prev
        while cur:
            if cur.val == val:
                if not cur.next:
                    prev.next = None
                    break
                prev.next = cur.next
                cur = prev.next
            else:
                prev, cur = cur, cur.next
        return res

print Solution().removeElements(ListNode.build([1, 2, 2, 1]), 2)

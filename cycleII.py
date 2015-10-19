from hkdsun.linkedlist import *

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow, fast = head, head

        while fast:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None

n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n2.next = n1

Solution().detectCycle(n1)

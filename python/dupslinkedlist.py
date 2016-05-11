from hkdsun.linkedlist import *


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head.next:
            return head
        h, prev, cur = head, head, head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev, cur = cur, cur.next
        return h

l = ListNode.build([1,1,2,3,3])
print Solution().deleteDuplicates(l)

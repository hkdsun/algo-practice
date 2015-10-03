# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        return self.iterative(head)

    def recursive(self, head, prev):
        if not head:
            return prev
        newhead, head.next = head.next, prev
        return self.recursive(newhead, head)

    def iterative(self, head):
        prev, cur = None, head
        while cur:
            oldprev = prev
            prev = cur
            oldnext = cur.next
            cur.next = oldprev
            cur = oldnext
        return prev


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4

print Solution().reverseList(n1).val

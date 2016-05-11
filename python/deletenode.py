from hkdsun.linkedlist import *


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node.next:
            return
        node.val = node.next.val
        node.next = node.next.next

head = ListNode.build([1, 2, 3, 4, 5])
cur = head
for i in range(2):
    cur=cur.next
print cur
Solution().deleteNode(cur)
print head

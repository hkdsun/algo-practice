# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "[" + str(self.val) + "->" + str(self.next) + "]"


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        sortedList = ListNode(head.val)
        cur = head.next
        while cur:
            h = sortedList
            if cur.val < h.val:
                tmp = ListNode(cur.val)
                tmp.next = h
                cur = cur.next
                sortedList = tmp
            else:
                prev = None
                while h and h.val <= cur.val:
                    prev = h
                    h = h.next
                tmp = ListNode(cur.val)
                tmp.next = h
                prev.next = tmp
                cur = cur.next

        return sortedList

l = map(lambda x: ListNode(x), [1, 1])
for i in range(len(l)-1):
    l[i].next = l[i+1]
i = Solution().insertionSortList(l[0])
print "--------"
print i

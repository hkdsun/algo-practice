# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def find_kth(self, head, k):
        """
        :type head: ListNode
        :type k:    int
        :rtype ListNode
        """
        return ListNode(-1)

k = 2
l = [x for x in range(1, 10)]
l = map(lambda x: ListNode(x), l)
for i in range(len(l)-1):
    l[i].next = l[i+1]
print Solution().find_kth(l[0], k).val == l[-k-1].val

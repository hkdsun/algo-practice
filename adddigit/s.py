import copy
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        while head:
            if head in dic:
                return True
            dic[head] = 0
            head = head.next
        return False
    def hasCycle2(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            head = fast
        return False


lis = [1, 2, 3, 4, 5]
nodes = map(lambda n: ListNode(n), lis)
for i, c in enumerate(nodes[:-1]):
    c.next = nodes[i+1]

nodes2 = copy.deepcopy(nodes)

nodes[len(nodes)-1].next = nodes[1]

print Solution().hasCycle(nodes[0])
print Solution().hasCycle(nodes2[0])
print Solution().hasCycle2(nodes[0])
print Solution().hasCycle2(nodes2[0])

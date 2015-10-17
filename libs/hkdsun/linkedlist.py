# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def _get_all_children(self):
        res, q = [], [self]
        while q:
            head = q.pop(0)
            res.append(head.val)
            if head.next:
                q.append(head.next)
        return res

    def __str__(self):
        children = self._get_all_children()
        return "->".join(map(str, children))

    @staticmethod
    def build(lis):
        if len(lis) == 0:
            return None
        lis = map(lambda x: ListNode(x), lis)
        for i in range(len(lis)-1):
            lis[i].next = lis[i+1]
        return lis[0]
